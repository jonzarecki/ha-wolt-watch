# Wolt Watch - Home Assistant Custom Integration

A Home Assistant custom integration that watches Wolt restaurants and sends notifications when they open. Perfect for getting notified when your favorite restaurant becomes available for delivery!

## ✨ Features

- 🍕 **Watch any Wolt restaurant** by entering its slug (from the Wolt URL)
- ⏰ **Configurable watch duration** (from 1 minute to 24 hours)
- 📱 **Mobile notifications** to any Home Assistant mobile app device
- 🎨 **Beautiful Lovelace card** with intuitive UI
- 🔧 **No configuration required** - works out of the box!

## 🚀 Installation

### HACS Installation (Recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click the three dots menu → "Custom repositories"
4. Add repository URL: `https://github.com/jzarecki/ha-wolt-watch`
5. Category: "Integration"
6. Click "Add"
7. Find "Wolt Watch" in HACS and install it
8. **Restart Home Assistant**

### Manual Installation

1. Download the latest release
2. Copy the `custom_components/wolt_watch` folder to your Home Assistant `custom_components` directory
3. Copy `www/wolt-watch-card.js` to your Home Assistant `www` directory
4. **Restart Home Assistant**

## 📖 Usage

### Adding the Card

1. Go to any Lovelace dashboard
2. Click "Edit Dashboard"
3. Click "Add Card"
4. Search for "Wolt Watch Card"
5. Add the card - no configuration needed!

### Using the Card

1. **Restaurant Slug**: Enter the restaurant identifier from the Wolt URL
   - Example: For `https://wolt.com/en/isr/tel-aviv/restaurant/taizu`, use `taizu`
   - Example: For `https://wolt.com/en/isr/tel-aviv/restaurant/mcdonalds-dizengoff`, use `mcdonalds-dizengoff`

2. **Watch Duration**: Set how long to monitor the restaurant (1 minute to 24 hours)

3. **Notification Device**: Select which mobile device should receive the notification

4. **Click "Start Watching"**: The integration will monitor the restaurant and notify you when it opens!

## 🔧 Advanced Configuration

### Manual Card Registration (if needed)

If the card doesn't appear automatically, add this to your `configuration.yaml`:

```yaml
lovelace:
  resources:
    - url: /local/wolt-watch-card.js
      type: module
```

### Integration Setup (usually automatic)

The integration loads automatically. If needed, you can explicitly enable it in `configuration.yaml`:

```yaml
wolt_watch:
```

## 🛠 Development

### Requirements

- Python 3.11+
- Home Assistant 2023.1+

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/jzarecki/ha-wolt-watch.git
cd ha-wolt-watch

# Create virtual environment
uv venv --python 3.11
source .venv/bin/activate

# Install development dependencies
uv pip install pytest pytest-cov pyyaml voluptuous
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=custom_components.wolt_watch --cov-report=term-missing

# Validate configuration files
python -c "import json; json.load(open('custom_components/wolt_watch/manifest.json')); print('✅ manifest.json valid')"
python -c "import json; json.load(open('hacs.json')); print('✅ hacs.json valid')"
python -c "import yaml; yaml.safe_load(open('custom_components/wolt_watch/services.yaml')); print('✅ services.yaml valid')"
```

## 📝 How It Works

1. **Restaurant Monitoring**: Uses the Wolt API to check if a restaurant is open
2. **Polling**: Checks every 30 seconds (with smart backoff on errors)
3. **Notification**: Sends a mobile notification when the restaurant opens
4. **Timeout**: Stops watching after the specified duration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python -m pytest tests/ -v`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 🐛 **Bug Reports**: [Open an issue](https://github.com/jzarecki/ha-wolt-watch/issues)
- 💡 **Feature Requests**: [Start a discussion](https://github.com/jzarecki/ha-wolt-watch/discussions)
- 📖 **Documentation**: [Project Wiki](https://github.com/jzarecki/ha-wolt-watch/wiki)

## 🎯 Roadmap

- [ ] Support for multiple restaurants simultaneously
- [ ] Restaurant status dashboard
- [ ] Integration with Home Assistant automations
- [ ] Support for more delivery platforms
- [ ] Restaurant availability history

---

Made with ❤️ for the Home Assistant community