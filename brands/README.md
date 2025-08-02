# Wolt Watch Brands

This directory contains brand assets for the Wolt Watch integration.

## Submission to Home Assistant Brands

To properly support this integration in HACS, these brand assets need to be submitted to the [home-assistant/brands](https://github.com/home-assistant/brands) repository.

### Required Files

- `icon.png` - 256x256 square icon
- `icon@2x.png` - 512x512 hDPI version (optional)
- `logo.png` - Landscape logo (optional, falls back to icon)
- `logo@2x.png` - hDPI logo version (optional)

### Requirements

1. **Format**: PNG only
2. **Optimization**: Properly compressed for web
3. **Transparency**: Preferred
4. **Background**: Optimized for white backgrounds
5. **Trimming**: Minimal empty space around the subject

### Submission Process

1. Fork the [home-assistant/brands](https://github.com/home-assistant/brands) repository
2. Add files to `custom_integrations/wolt_watch/`
3. Follow their contribution guidelines
4. Submit a pull request

### Current Status

🚧 **Placeholder files only** - Real brand assets need to be created and submitted.

For HACS validation, you may need to temporarily ignore the "brands" check until proper assets are submitted:

```yaml
# In GitHub workflow
- name: HACS validation
  uses: "hacs/action@main"
  with:
    category: "integration"
    ignore: "brands"
```