#!/usr/bin/env python3
"""Check project documentation names, local Markdown links, and heading anchors.

Copied and installed skill bundles are excluded. Project-owned skills are checked
for links, but their SKILL.md filenames are preserved.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OWNED_SKILLS = {'inventory-truth', 'kapso-kaseis', 'obra-onboarding', 'scope-gate'}


def included(path):
    relative = path.relative_to(ROOT)
    if '.git' in relative.parts or '.agents' in relative.parts:
        return False
    if relative.parts[:2] == ('.cursor', 'skills'):
        return len(relative.parts) > 2 and relative.parts[2] in OWNED_SKILLS
    return path.suffix in {'.md', '.mdc'}


def prose(path):
    # Ignore code examples so template links do not become false failures.
    return re.sub(r'^\s*(`{3,}|~{3,}).*?^\s*\1\s*$', '',
                  path.read_text(), flags=re.M | re.S)


def anchors(path):
    found = set()
    repeats = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose(path), re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = repeats.get(slug, 0)
        repeats[slug] = count + 1
        found.add(f'{slug}-{count}' if count else slug)
    found.update(re.findall(r'(?:id|name)=["\']([^"\']+)', prose(path)))
    return found


def main():
    errors = []
    count = 0
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and included(p))
    for path in files:
        relative = path.relative_to(ROOT)
        if path.suffix == '.md' and not re.fullmatch(r'[A-Z0-9]+(?:_[A-Z0-9]+)*\.md', path.name):
            errors.append(f'{relative}: filename is not UPPER_SNAKE_CASE')
        source = prose(path)
        targets = re.findall(r'!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["\'][^\n]*?["\'])?\s*\)', source)
        targets += re.findall(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', source, re.M)
        for raw in targets:
            target = urlsplit(raw.strip('<>'))
            if target.scheme or target.netloc:
                continue
            count += 1
            local = (path.parent / unquote(target.path)).resolve() if target.path else path
            if not local.exists():
                errors.append(f'{relative}: missing {raw}')
            elif target.fragment and local.is_file() and local.suffix in {'.md', '.mdc'}:
                if unquote(target.fragment) not in anchors(local):
                    errors.append(f'{relative}: missing anchor {raw}')
    for error in errors:
        print(error, file=sys.stderr)
    print(f'Checked {len(files)} project documents, {count} relative links: {len(errors)} errors.')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
