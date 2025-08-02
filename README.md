# Wolt Watch - Home Assistant Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]

![Project Maintenance][maintenance-shield]
[![GitHub Release Date][releases-date-shield]][releases]

[![Community Forum][forum-shield]][forum]

_Integration to watch Wolt restaurants and get notified when they open._

## Quick Start

**Installation via HACS (Recommended):**

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=jonzarecki&repository=ha-wolt-watch&category=integration)

**Add Dashboard Card:**

[![Open your Home Assistant instance and show the dashboard with a specific view.](https://my.home-assistant.io/badges/lovelace_dashboard.svg)](https://my.home-assistant.io/redirect/lovelace/default_view?show_add_card&card_type=custom:wolt-watch-card)

## About

Wolt Watch provides a simple one-click way to monitor when your favorite Wolt restaurants change from closed to open status. Perfect for those special restaurants that have limited hours or unpredictable opening times.

### Features

- 🍕 **One-click restaurant monitoring** - Just enter the restaurant slug and start watching
- 📱 **Mobile notifications** - Get push notifications directly to your phone
- ⏰ **Configurable duration** - Set how long to watch (default 2 hours)
- 🧹 **No persistent entities** - Keeps your Home Assistant instance clean
- 🎯 **Dashboard integration** - Easy-to-use Lovelace card
- 🔒 **Bronze Quality Tier** - Meets Home Assistant integration quality standards
- 🛡️ **Type Safe** - Full type annotations for better reliability
- 🧪 **Tested** - Includes automated tests for core functionality

## Installation

### HACS (Recommended)

1. **Install the repository**:
   - Click the badge above or manually add this repository to HACS
   - Restart Home Assistant

2. **Add the dashboard card**:
   - Go to your dashboard in edit mode
   - Click "Add Card" → Search for "Wolt Watch Card"
   - Add the card to your dashboard

### Manual Installation

1. Copy the `custom_components/wolt_watch` directory to your Home Assistant's `custom_components` directory
2. Copy `www/wolt-watch-card.js` to your `www` directory  
3. Add the card resource in your dashboard configuration:
   ```yaml
   resources:
     - url: /local/wolt-watch-card.js
       type: module
   ```
4. Restart Home Assistant

## Usage

### Using the Dashboard Card

1. **Find your restaurant slug**: 
   - Go to Wolt website/app
   - Navigate to your desired restaurant
   - Copy the slug from the URL (e.g., `taizu`, `mcdonalds-dizengoff`)

2. **Configure the watch**:
   - Enter the restaurant slug
   - Set how long to watch (default 2 hours)
   - Select your mobile device for notifications

3. **Start watching**: Click "Start Watching" and you'll get a notification when the restaurant opens

### Using the Service Directly

You can also call the service directly in automations or scripts:

```yaml
service: wolt_watch.start
data:
  slug: "taizu"
  timeout_m: 30  # 30 minutes
  device: "notify.mobile_app_iphone"
```

### Service Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `slug` | string | Yes | - | Restaurant identifier from Wolt URL |
| `timeout_m` | integer | No | 30 | Watch duration in minutes (1-1440) |
| `device` | string | Yes | - | Notify service entity (e.g., `notify.mobile_app_*`) |

## Finding Restaurant Slugs

Restaurant slugs can be found in the Wolt URL. For example:
- `https://wolt.com/en/isr/tel-aviv/restaurant/taizu` → slug is `taizu`
- `https://wolt.com/en/isr/tel-aviv/restaurant/mcdonalds-dizengoff` → slug is `mcdonalds-dizengoff`

## How It Works

1. **Polling**: The integration polls the Wolt API every 60 seconds
2. **State tracking**: It remembers if the restaurant was already open to avoid duplicate notifications
3. **Smart notifications**: Only sends notification on the first "closed → open" transition
4. **Auto cleanup**: Tasks automatically terminate after timeout or successful notification

## Troubleshooting

### Common Issues

**Integration not loading:**
- Check that `wolt-sdk` is properly installed: `pip install wolt-sdk`
- Verify all files are in the correct directories
- Check Home Assistant logs for error messages
- Restart Home Assistant after installation

**No notifications received:**
- Verify your mobile device entity ID is correct (check Developer Tools → States)
- Check that Mobile App integration is working
- Test notifications with Developer Tools → Services
- Ensure device format is correct: `notify.mobile_app_yourdevice`

**Restaurant not found:**
- Double-check the restaurant slug from the Wolt URL
- Ensure the restaurant is available in your location
- Try a different restaurant to test functionality
- Check if the restaurant has regular opening hours

**HACS Installation Issues:**
- Ensure you have HACS installed and configured
- Check that your Home Assistant version is 2024.1.0 or newer
- Clear browser cache if the integration doesn't appear in UI

### Debug Logging

To enable debug logging, add this to your `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.wolt_watch: debug
```

## Rate Limiting

The integration is designed to be respectful of Wolt's API:
- Polls every 60 seconds (configurable in code)
- Backs off to 90 seconds on API errors
- Terminates automatically to avoid indefinite polling

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- Built by [jonzarecki](https://github.com/jonzarecki)
- Uses [wolt-sdk](https://pypi.org/project/wolt-sdk/) for Wolt API integration
- Inspired by the Home Assistant community's need for restaurant monitoring

---

[commits-shield]: https://img.shields.io/github/commit-activity/y/jonzarecki/ha-wolt-watch.svg?style=for-the-badge
[commits]: https://github.com/jonzarecki/ha-wolt-watch/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/jonzarecki/ha-wolt-watch.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40jonzarecki-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/jonzarecki/ha-wolt-watch.svg?style=for-the-badge
[releases]: https://github.com/jonzarecki/ha-wolt-watch/releases
[releases-date-shield]: https://img.shields.io/github/release-date/jonzarecki/ha-wolt-watch.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/