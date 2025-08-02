# Contributing to Wolt Watch

Thank you for your interest in contributing to Wolt Watch! We welcome contributions from the community.

## Ways to Contribute

- **Bug Reports**: Report bugs and issues you encounter
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit pull requests with fixes or new features
- **Documentation**: Improve documentation and examples
- **Testing**: Help test the integration with different configurations

## Getting Started

### Prerequisites

- Python 3.11+
- Home Assistant 2024.1.0+
- Git
- A GitHub account

### Development Setup

1. **Fork the repository** on GitHub

2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/jonzarecki/ha-wolt-watch.git
   cd ha-wolt-watch
   ```

3. **Set up Home Assistant development environment**:
   - Follow the [Home Assistant development guide](https://developers.home-assistant.io/docs/development_environment/)
   - Copy the `custom_components/wolt_watch` directory to your HA config

4. **Install dependencies**:
   ```bash
   pip install wolt-sdk
   ```

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the guidelines below

3. **Test your changes** thoroughly

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

## Development Guidelines

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use type hints where appropriate
- Add docstrings for functions and classes
- Use meaningful variable and function names

### JavaScript/Frontend

- Follow modern JavaScript ES6+ standards
- Use LitElement patterns for custom cards
- Maintain compatibility with Home Assistant frontend components

### Testing

- Test your changes with a real Home Assistant instance
- Verify the integration loads without errors
- Test both success and error scenarios
- Validate the Lovelace card displays and functions correctly

### Documentation

- Update README.md if adding new features
- Update service descriptions in services.yaml
- Add code comments for complex logic
- Include examples for new functionality

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] PR targets the `main` branch

### PR Description

Please include:
- **What** changes you made
- **Why** you made these changes
- **How** to test the changes
- Any **breaking changes** or special considerations

### Review Process

1. Automated checks will run (HACS validation, etc.)
2. Maintainers will review your code
3. Address any feedback or requested changes
4. Once approved, your PR will be merged

## Reporting Issues

### Bug Reports

Please include:
- Home Assistant version
- Integration version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant log messages
- Configuration details (sanitized)

### Feature Requests

Please include:
- Clear description of the feature
- Use case or problem it solves
- Proposed implementation (if you have ideas)
- Any alternatives you've considered

## Community Guidelines

- Be respectful and inclusive
- Help others learn and contribute
- Follow the [Home Assistant Code of Conduct](https://github.com/home-assistant/core/blob/dev/CODE_OF_CONDUCT.md)
- Search existing issues before creating new ones

## Getting Help

- Check the [README](README.md) for basic usage
- Review existing [issues](https://github.com/jonzarecki/ha-wolt-watch/issues)
- Ask questions in the [Home Assistant Community Forum](https://community.home-assistant.io/)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes for significant contributions
- README credits section

Thank you for contributing to Wolt Watch! 🍕