# NDIS case file (private)

Full copy of the NDIS case folder: original files, byte-identical, with their original names and folder layout.

## Finding things
- Full file list with SHA-256 checksums: `00_INDEX/SHA256SUMS.txt`
- Search everything: `git grep -i "term"` (text files) or ripgrep (`rg -i "term"`).
- Three large files are in Git LFS. After cloning, run `git lfs pull` before searching them:
  - `20240613 Tender Bundle [Finalised] 23004627.pdf` (108 MB)
  - `ART_FOI_2026-1839/11 - T-documents for case 2023.3361.pdf` (63 MB)
  - `Chronology/NDIS_Case_Database.sqlite` (91 MB): the chronology database

## Privilege
Some folders contain material marked privileged (for example the counsel brief and counsel instructions). Storing privileged material on a third-party host may create a privilege-waiver argument. Confirm with counsel before sharing this repo with anyone.

## Access
Repo is PRIVATE. Keep the collaborator list minimal.
