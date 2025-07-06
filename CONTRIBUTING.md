
# Contributing to Temple Analytics

Thank you for your interest in contributing to Temple Analytics! We welcome all contributions that help improve and grow the project. This document provides guidelines for contributing code, documentation, and ideas to ensure a smooth collaboration process.

---

## How to Contribute

### 1. Fork the Repository
Create a personal fork of the repository on GitHub and clone it to your local machine:

```bash
git clone [https://github.com/YOUR_USERNAME/temple-analytics.git](https://github.com/Temple-Analytics/TempleAnalyticsAI.git)
cd temple-analytics
```

Add the original repository as a remote to keep your fork updated:

```bash
git remote add upstream [https://github.com/Temple-Analytics/temple-analytics.git](https://github.com/Temple-Analytics/TempleAnalyticsAI.git)
```

---

### 2. Create a Branch
Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

---

### 3. Make Changes
- Follow the existing code style and conventions.
- Write clear, concise commit messages.
- Include tests if applicable.
- Ensure your changes do not break existing functionality.

---

### 4. Run Tests
Before submitting a pull request, run all tests to ensure nothing is broken:

```bash
pytest tests/
```

---

### 5. Submit a Pull Request
Push your branch to your fork and open a pull request (PR) on GitHub:

```bash
git push origin feature/your-feature-name
```

When opening a PR:
- Clearly describe your changes.
- Reference any related issues with `#issue_number`.
- Indicate whether the PR is a work in progress (WIP) or ready for review.

---

## Contribution Guidelines

- **Code Style**: Follow PEP 8 for Python code and use consistent formatting for other languages in the project.
- **Commits**: Use meaningful commit messages. Example: `fix: correct API error handling` or `feat: add portfolio analytics feature`.
- **Issues**: Search for existing issues before opening a new one. If you open an issue, provide detailed steps to reproduce bugs or describe feature requests clearly.
- **Tests**: Add tests for new features and bug fixes whenever possible.

---

## Reporting Bugs or Requesting Features

1. Check the existing [issues](https://github.com/Temple-Analytics/temple-analytics/issues) to see if your bug or feature is already discussed.
2. Open a new issue if necessary and provide:
   - A clear description of the bug or feature request.
   - Steps to reproduce the bug (if applicable).
   - Any relevant logs or screenshots.

---

## Community Standards

- Be respectful and constructive in all interactions.
- Help us maintain a welcoming and inclusive environment for all contributors.

---

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
