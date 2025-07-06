
# 🔐 DuskCipher Pro Toolkit v3.0

[![Version](https://img.shields.io/badge/version-3.0-blue.svg)](https://github.com/duskcipher/toolkit)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-yellow.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](https://github.com/duskcipher/toolkit)

> **Professional Encryption Toolkit** - Advanced Script Protection & Obfuscation System

## 🌟 Features

### 🔒 Core Encryption
- **Advanced Script Encryption** - Military-grade protection for bash scripts
- **Smart Decryption** - Intelligent restoration of original files
- **Batch Operations** - Process multiple files simultaneously
- **Auto-Backup** - Automatic backup before encryption

### 📊 Advanced Analytics
- **File Analyzer** - Comprehensive file analysis with detailed metrics
- **Security Scanner** - Vulnerability assessment and security checks
- **Integrity Verification** - File integrity monitoring with checksums
- **Usage Statistics** - Detailed usage tracking and reporting

### 🛠️ System Tools
- **System Monitor** - Real-time system information and process monitoring
- **Network Tools** - Network configuration and connectivity analysis
- **Disk Management** - Storage analysis and usage optimization
- **Environment Manager** - Environment variable management

### 🎨 Customization
- **Theme System** - Multiple color schemes and UI themes
- **Configuration Manager** - Persistent settings and preferences
- **User Profiles** - Personalized user experience
- **Export/Import** - Configuration backup and restoration

### 💾 Backup & Recovery
- **Smart Backup** - Automated backup with timestamp tracking
- **Restore Manager** - Easy file restoration from backups
- **Cleanup Tools** - Automatic old backup cleanup
- **Backup Statistics** - Detailed backup analysis and reporting

## 🚀 Quick Start

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/duskcipher/pro-encShell.git
   cd pro-encShell
   ```

2. **Run the installer**:
   ```bash
   bash install.sh
   ```

3. **Launch the application**:
   ```bash
   python3 main.py
   ```

### First Steps

1. **Create a test script**:
   ```bash
   nano test_script.sh
   ```
   Add some bash commands and save.

2. **Encrypt your script**:
   - Select `[1] 🔒 ENCRYPT SCRIPT`
   - Choose your script file
   - Enter output filename
   - Your script is now protected!

3. **Analyze files**:
   - Select `[3] 📊 FILE ANALYZER`
   - View detailed file information
   - Check file integrity and security

## 📖 Detailed Usage

### Encryption Operations

#### Basic Encryption
```bash
# Launch the tool
python3 main.py

# Select encryption option [1]
# Choose your script file
# Enter output filename
# Tool will automatically encrypt your script
```

#### Batch Encryption
```bash
# Select batch operations [4]
# Choose "Encrypt All Files" [1]
# All .sh files will be encrypted with _encrypted suffix
```

### Security Features

#### Security Scanner
The built-in security scanner checks for:
- **Dangerous Commands** - `rm -rf`, `chmod 777`, etc.
- **Code Injection** - `eval $`, dynamic execution
- **Insecure Practices** - Hardcoded passwords, API keys
- **Network Risks** - Piping curl/wget to bash

#### File Integrity
- **SHA256 Checksums** - Automatic checksum generation
- **Change Detection** - Monitor file modifications
- **Integrity Reports** - Detailed integrity analysis

### System Tools

#### System Monitor
- **Process Information** - Real-time process monitoring
- **Resource Usage** - CPU, memory, disk usage
- **Network Status** - Interface and connectivity info
- **System Statistics** - Comprehensive system metrics

#### Environment Management
- **Variable Tracking** - Important environment variables
- **Path Analysis** - PATH variable breakdown
- **Shell Information** - Shell configuration details

### Backup & Recovery

#### Automatic Backups
- **Timestamp Naming** - Files backed up with timestamps
- **Incremental Backups** - Only changed files are backed up
- **Retention Policy** - Automatic cleanup of old backups
- **Restore Points** - Easy restoration to previous versions

#### Backup Management
- **Backup Browser** - View all available backups
- **Selective Restore** - Restore specific files
- **Backup Statistics** - Storage usage and file counts
- **Cleanup Tools** - Remove old or unnecessary backups

## 🎯 Advanced Features

### Configuration System
```json
{
  "version": "3.0",
  "author": "./B7",
  "community": "DuskCipher",
  "theme": "dark",
  "auto_backup": true,
  "encryption_method": "advanced",
  "log_level": "info",
  "stats": {
    "files_encrypted": 0,
    "files_decrypted": 0,
    "total_runs": 0
  }
}
```

### Logging System
- **Automatic Logging** - All operations are logged
- **Log Levels** - Debug, Info, Warning, Error
- **Log Rotation** - Daily log files with rotation
- **Log Analysis** - Built-in log viewer and analysis

### Statistics & Reporting
- **Usage Metrics** - Track tool usage patterns
- **Performance Stats** - Operation timing and success rates
- **File Analytics** - File type distribution and sizes
- **Security Reports** - Vulnerability scan results

## 🔧 Configuration

### Customization Options

#### Change Author/Community
```bash
# Select [8] 🎨 CUSTOMIZATION
# Choose [1] Change Author Name
# Enter new author name
# Configuration is automatically saved
```

#### Backup Settings
```bash
# Select [8] 🎨 CUSTOMIZATION
# Choose [3] Toggle Auto Backup
# Auto backup is enabled/disabled
```

#### Log Level
```bash
# Select [8] 🎨 CUSTOMIZATION
# Choose [4] Change Log Level
# Select: debug, info, warning, error
```

### Directory Structure
```
DuskCipher-Pro/
├── main.py                 # Main application
├── index.sh               # Shell launcher
├── install.sh             # Installation script
├── config/
│   ├── duskcipher.json    # Main configuration
│   └── colors.sh          # Color definitions
├── logs/
│   └── duskcipher_*.log   # Daily log files
├── backups/
│   └── *_timestamp.sh     # Backup files
├── test_scripts/
│   └── advanced_test.sh   # Sample scripts
└── docs/
    ├── GUIDE.md           # User guide
    └── CHANGELOG.md       # Change log
```

## 🛡️ Security

### Encryption Methods
- **Base64 Encoding** - Basic obfuscation
- **bash-obfuscate** - Advanced script obfuscation
- **Custom Algorithms** - Proprietary encryption methods
- **Multi-layer Protection** - Multiple encryption passes

### Security Best Practices
- **Backup Before Encryption** - Always backup original files
- **Verify Encrypted Files** - Test encrypted scripts before deployment
- **Regular Security Scans** - Use built-in security scanner
- **Keep Tools Updated** - Regular updates for security patches

## 📊 Statistics

### Usage Tracking
- **Total Runs** - Application launch count
- **Files Processed** - Encryption/decryption statistics
- **Success Rates** - Operation success percentages
- **Time Tracking** - Operation duration analysis

### Performance Metrics
- **File Sizes** - Track processed file sizes
- **Processing Speed** - Operations per second
- **Memory Usage** - Memory consumption patterns
- **Error Rates** - Error frequency and types

## 🔄 Updates & Maintenance

### Auto-Update System
- **Version Checking** - Automatic version detection
- **Update Notifications** - New version alerts
- **Incremental Updates** - Only changed files updated
- **Rollback Support** - Revert to previous versions

### Maintenance Tools
- **Log Cleanup** - Automatic log file rotation
- **Cache Management** - Temporary file cleanup
- **Configuration Validation** - Settings verification
- **Dependency Check** - Required package verification

## 🚨 Troubleshooting

### Common Issues

#### Encryption Fails
```bash
# Check if bash-obfuscate is installed
which bash-obfuscate

# Install if missing
npm install bash-obfuscate

# Try encryption again
```

#### Permission Errors
```bash
# Fix file permissions
chmod +x script.sh

# Check directory permissions
ls -la backups/
```

#### Configuration Issues
```bash
# Reset configuration
# Select [8] 🎨 CUSTOMIZATION
# Choose [5] Reset Statistics
# This will reset all settings
```

### Error Codes
- **E001** - File not found
- **E002** - Permission denied
- **E003** - Encryption tool missing
- **E004** - Configuration error
- **E005** - Network error

## 📞 Support

### Getting Help
1. **Built-in Help** - Use the help system in the application
2. **Documentation** - Check the docs/ directory
3. **Log Files** - Review log files for error details
4. **Community** - Join the DuskCipher community

### Reporting Issues
- **Error Logs** - Include relevant log files
- **System Info** - Provide system information
- **Steps to Reproduce** - Detailed reproduction steps
- **Screenshots** - Visual error representations

## 👨‍💻 Author

**./B7**
- 🌟 Professional Tool Developer
- 🔐 Security & Encryption Specialist
- 📧 Contact: [Your Contact Information]

## 🙏 Acknowledgments

- **DuskCipher** community
- **bash-obfuscate** community
- **Open source** contributors
- **Security research** community

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Changelog

### Version 3.0 (Current)
- ✨ Complete UI overhaul with enhanced colors
- 🚀 Added batch operations for multiple files
- 🔍 Integrated security scanner with vulnerability detection
- 📊 Advanced file analyzer with detailed metrics
- 🛠️ System tools for monitoring and management
- 🎨 Customization system with themes and preferences
- 💾 Comprehensive backup and recovery system
- 📈 Statistics and usage tracking
- 🔧 Configuration management system
- 📝 Enhanced logging and error handling

### Version 2.0
- 🔒 Advanced encryption algorithms
- 📁 File management improvements
- 🎯 Better user interface
- 🔄 Auto-backup functionality

### Version 1.0
- 🚀 Initial release
- 🔐 Basic encryption/decryption
- 📊 Simple file analysis
- 🛡️ Core security features

---

<div align="center">

**Made with ❤️ by ./B7 & DuskCipher Community**

[⭐ Star this project](https://github.com/duskcipher/toolkit) | [🐛 Report Bug](https://github.com/duskcipher/toolkit/issues) | [💡 Request Feature](https://github.com/duskcipher/toolkit/issues)

</div>
