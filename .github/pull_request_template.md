## Summary
<!-- Briefly describe the changes made in this pull request. -->

## Checklist

General
- [ ] Tested potentially affected functionalities locally
- [ ] Live demoed to reviewer
- [ ] If any, used environment variables for configurations that can't be exposed or needs value adjustment later
- [ ] If any, named new environment variables with its function group in front: e.g. CARBONNEWS_xxx
- [ ] If any, reused components instead of creating new ones. Even if the old component is not designed for new function purpose, it is refactored/generalised instead of reinventing the wheel.

Frontend:
- [ ] If any, tailwindCSS is used wherever possible
- [ ] If any, existing file and variable naming conventions are used.

Backend:
- [ ] Avoided unnecessarily complicated logic by using simpler logic
- [ ] Debug tracing is added for using AWS x-ray service

Database:
- [ ] If any, have minimised the to and fro with database to a single transaction per function call
- [ ] If any, when using SQL raw query, only retrieving the columns you need

## Screenshots (if applicable)

...

## Related Issues
<!-- Closes #123 -->
