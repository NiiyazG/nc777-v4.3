# Browser QA Playbook

Use only when `browser_ui: true` and the current risk involves UI/runtime behavior.

Choose the cheapest meaningful checks:
- render and critical interaction path;
- console/runtime errors;
- failed/incorrect network requests;
- state persistence/storage only where relevant;
- keyboard navigation and visible focus;
- accessible name/label for interactive controls;
- contrast/readability only if visual accessibility is in scope;
- responsive/boundary viewport if layout risk changed.

Do not require Playwright/Chrome specifically. Existing project test tooling, browser automation, manual observation or equivalent evidence are all acceptable when appropriate.

Record what was not checked (browser matrix, assistive technology, mobile device, visual diff, etc.).
