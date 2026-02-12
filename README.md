# HelloWorld Next.js + Selenium + Allure (GitHub Pages)

This demo repository is intentionally minimal so you can quickly see Allure working.

It contains:
- A static Next.js website (`HelloWorld`)
- Python Selenium UI tests (1 pass + 1 intentional fail)
- A **manual** GitHub Actions workflow that:
  1. Builds the Next.js static site
  2. Runs Selenium tests
  3. Builds Allure report
  4. Publishes report to `gh-pages`

---

## 1) Create a new public GitHub repo

Create an empty public repo (no README/license needed).

---

## 2) Upload this project

Copy all files from this demo into your new repo and push to `main`.

---

## 3) Enable workflow write permissions

In your repo:

`Settings -> Actions -> General -> Workflow permissions -> Read and write permissions`

Save.

---

## 4) Enable GitHub Pages

In your repo:

`Settings -> Pages`

- Source: **Deploy from a branch**
- Branch: **gh-pages**
- Folder: **/(root)**

Save.

---

## 5) Run the workflow manually

Go to:

`Actions -> Next.js UI tests + Allure report (manual) -> Run workflow`

The workflow is manual-only (`workflow_dispatch`).

---

## 6) Open your Allure report

After the run finishes, open:

`https://<your-github-username>.github.io/<your-repo-name>/`

You should see one passed and one failed test in the report.

---

## Notes

- The failing test is intentional so the Allure report shows both success and failure.
- Even if tests fail, report publishing still runs (`if: always()`).
