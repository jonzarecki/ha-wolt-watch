# Wolt Watch Integration

Watch your favorite Wolt restaurants and get notified when they open!

## Features

- 🍕 **One-click restaurant monitoring** - Just enter the restaurant slug and start watching
- 📱 **Mobile notifications** - Get push notifications directly to your phone  
- ⏰ **Configurable duration** - Set how long to watch (default 2 hours)
- 🧹 **No persistent entities** - Keeps your Home Assistant instance clean
- 🎯 **Dashboard integration** - Easy-to-use Lovelace card

## Quick Setup

1. Install via HACS
2. Restart Home Assistant
3. Add the Wolt Watch card to your dashboard
4. Start watching your favorite restaurants!

## How to Use

1. **Find the restaurant slug** from the Wolt URL
   - Example: `https://wolt.com/en/isr/tel-aviv/restaurant/taizu` → slug is `taizu`

2. **Configure your watch**:
   - Enter the restaurant slug
   - Set watch duration (default 2 hours)
   - Select your mobile device

3. **Start watching** and get notified when it opens!

## Requirements

- Home Assistant 2024.1.0+
- Mobile App integration configured
- Internet connection

The integration automatically installs the required `wolt-sdk` dependency.