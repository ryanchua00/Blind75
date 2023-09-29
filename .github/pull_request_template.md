## Summary
<!-- Briefly describe the changes made in this pull request. -->

## Checklist

General
- [ ] tested potentially affected functionalities locally
- [ ] live demoed to reviewer
- [ ] used environment variable for configurations that can not be exposed or needs value adjustment later
- [ ] if any, named new environment variable with its function group in front: e.g. CARBONNEWS_xxx
- [ ] reused components instead of creating a new one. Even if the old component is not designed for new function purpose, it is refactored/generalised instead of reinventing the wheel

Frontend:
- [ ] tailwindCSS is used wherever possible

Backend:
- [ ] unnecessarily complicated logic is avoided by using simpler logic
- [ ] debug tracing is added for using AWS x-ray service

Database:
- [ ] have minimised the to and fro with database to a single transaction per function call
- [ ] when using SQL raw query, only retrieving the columns you need

## Screenshots (if applicable)

...

## Related Issues
<!-- Closes #123 -->
