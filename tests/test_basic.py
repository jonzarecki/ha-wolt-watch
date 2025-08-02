"""Basic tests for Wolt Watch project structure."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def test_project_structure():
    """Test that the project has the correct structure."""
    root_dir = Path(__file__).parent.parent
    
    # Check main directories
    assert (root_dir / "custom_components").exists()
    assert (root_dir / "custom_components" / "wolt_watch").exists()
    assert (root_dir / "www").exists()
    assert (root_dir / ".github").exists()
    assert (root_dir / "tests").exists()
    
    # Check main files
    assert (root_dir / "README.md").exists()
    assert (root_dir / "LICENSE").exists()
    assert (root_dir / "hacs.json").exists()
    assert (root_dir / "VERSION").exists()


def test_hacs_json():
    """Test that hacs.json is valid and has required fields."""
    root_dir = Path(__file__).parent.parent
    hacs_path = root_dir / "hacs.json"
    
    assert hacs_path.exists()
    
    with open(hacs_path) as f:
        hacs_config = json.load(f)
    
    # Check required fields
    assert "name" in hacs_config
    assert "country" in hacs_config
    
    # Check values
    assert hacs_config["name"] == "Wolt Watch"
    assert hacs_config["country"] == "IL"


def test_version_file():
    """Test that VERSION file exists and contains a valid version."""
    root_dir = Path(__file__).parent.parent
    version_path = root_dir / "VERSION"
    
    assert version_path.exists()
    
    with open(version_path) as f:
        version = f.read().strip()
    
    # Basic version format check (semantic versioning)
    assert version.count(".") >= 2  # Should have at least major.minor.patch
    assert version[0].isdigit()  # Should start with a number


def test_readme_exists():
    """Test that README.md exists and is not empty."""
    root_dir = Path(__file__).parent.parent
    readme_path = root_dir / "README.md"
    
    assert readme_path.exists()
    
    with open(readme_path) as f:
        content = f.read()
    
    assert len(content) > 100  # Should have substantial content
    assert "Wolt Watch" in content
    assert "HACS" in content


def test_license_exists():
    """Test that LICENSE file exists."""
    root_dir = Path(__file__).parent.parent
    license_path = root_dir / "LICENSE"
    
    assert license_path.exists()
    
    with open(license_path) as f:
        content = f.read()
    
    assert "MIT" in content
    assert len(content) > 100


def test_github_workflows():
    """Test that GitHub workflows exist."""
    root_dir = Path(__file__).parent.parent
    workflows_dir = root_dir / ".github" / "workflows"
    
    assert workflows_dir.exists()
    assert (workflows_dir / "validate.yml").exists()
    assert (workflows_dir / "hassfest.yml").exists()
    assert (workflows_dir / "release.yml").exists()


def test_www_directory():
    """Test that www directory contains the Lovelace card."""
    root_dir = Path(__file__).parent.parent
    www_dir = root_dir / "www"
    
    assert www_dir.exists()
    assert (www_dir / "wolt-watch-card.js").exists()
    
    # Check that the card file is not empty
    card_path = www_dir / "wolt-watch-card.js"
    with open(card_path) as f:
        content = f.read()
    
    assert len(content) > 1000  # Should have substantial content
    assert "WoltWatchCard" in content
    assert "LitElement" in content