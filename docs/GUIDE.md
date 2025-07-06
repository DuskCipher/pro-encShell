
# UCH-2009 Encrypt/Decrypt Tools - User Guide 📖

> Comprehensive guide for using UCH-2009 professional encryption/decryption tools

## 📋 Table of Contents

1. [Quick Start](#-quick-start)
2. [Installation](#-installation)
3. [Basic Usage](#-basic-usage)
4. [Advanced Features](#-advanced-features)
5. [Troubleshooting](#-troubleshooting)
6. [Best Practices](#-best-practices)
7. [FAQ](#-faq)

## 🚀 Quick Start

Get up and running in under 5 minutes:

```bash
# 1. Start the application
bash index.sh

# 2. Choose option [1] to create a new script
# 3. Write your bash script in nano editor
# 4. Choose option [2] to access encryption tools
# 5. Select [1] Encrypt to protect your script
```

## 🔧 Installation

### Automatic Installation (Recommended)

```bash
bash install.sh
```

The installer will:
- ✅ Check system requirements
- ✅ Install Node.js dependencies
- ✅ Setup bash-obfuscate
- ✅ Create sample test scripts
- ✅ Verify all components

### Manual Installation

1. **Install Node.js dependencies**:
   ```bash
   npm install -g bash-obfuscate
   ```

2. **Verify Python**:
   ```bash
   python3 --version
   ```

3. **Check nano editor**:
   ```bash
   nano --version
   ```

## 📖 Basic Usage

### Creating Your First Script

1. **Launch the application**:
   ```bash
   bash index.sh
   ```

2. **Create new script**:
   - Select `[1] BUAT SCRIPT BARU`
   - Enter filename: `myfirst.sh`
   - Write your bash code in nano:
     ```bash
     #!/bin/bash
     echo "Hello, this is my first script!"
     echo "Current date: $(date)"
     ```
   - Save with `Ctrl+O` and exit with `Ctrl+X`

3. **Encrypt your script**:
   - Select `[2] LANGSUNG KE TOOLS`
   - Choose `[1] Encrypt`
   - Source file: `myfirst.sh`
   - Output file: `myfirst_encrypted.sh`

### Decrypting Scripts

1. **Access tools**:
   ```bash
   bash index.sh
   ```

2. **Choose decrypt option**:
   - Select `[2] LANGSUNG KE TOOLS`
   - Choose `[2] Decrypt`
   - Encrypted file: `myfirst_encrypted.sh`
   - Output file: `myfirst_decrypted.sh`

## 🔥 Advanced Features

### File Management

**View Available Files**:
```bash
# From main menu, select [3] LIHAT FILE YANG TERSEDIA
```

**File Information Display**:
- File size
- Last modified date
- File permissions
- Quick access options

### Script Templates

The tools include several pre-built templates:

1. **Basic Script** (`coba.sh`):
   - Simple demonstration script
   - Basic functions and loops
   - Good for testing

2. **Function Test** (`test_function.sh`):
   - Advanced function examples
   - Parameter handling
   - Return value testing

3. **Loop Test** (`test_loop.sh`):
   - Various loop structures
   - Array processing
   - Iteration examples

### Batch Operations

**Multiple File Encryption**:
```bash
# Create a batch script
for script in *.sh; do
    if [[ "$script" != "install.sh" && "$script" != "index.sh" ]]; then
        echo "Encrypting: $script"
        # Use tools to encrypt each file
    fi
done
```

## 🛠️ Troubleshooting

### Common Issues

**1. "bash-obfuscate not found"**
```bash
# Solution 1: Reinstall globally
npm install -g bash-obfuscate

# Solution 2: Use local installation
npm install bash-obfuscate
```

**2. "Permission denied"**
```bash
# Fix file permissions
chmod +x your_script.sh
```

**3. "File not found"**
- Ensure you're in the correct directory
- Check file name spelling
- Use tab completion for accuracy

**4. "Encryption failed"**
- Verify source file exists and is readable
- Check available disk space
- Ensure output directory is writable

### Debug Mode

Enable verbose logging:
```bash
# Set debug environment
export UCH_DEBUG=1
bash index.sh
```

### Log Files

Check logs for detailed error information:
```bash
# View error logs (if available)
cat ./logs/error.log

# View operation history
cat ./logs/operation.log
```

## ✨ Best Practices

### 🔒 Security

1. **Always backup original scripts** before encryption
2. **Test encrypted scripts** in isolated environment
3. **Use descriptive filenames** for easy identification
4. **Keep source files secure** after encryption
5. **Regularly update tools** for latest security features

### 📁 File Organization

```
your_project/
├── original_scripts/     # Your source files
├── encrypted_scripts/    # Encrypted versions
├── backups/             # Automatic backups
└── logs/                # Operation logs
```

### 🚀 Performance

1. **Use specific output names** for better tracking
2. **Clean up temporary files** regularly
3. **Monitor disk space** for large scripts
4. **Test on small files first** before bulk operations

### 🔄 Workflow

**Recommended Development Cycle**:
1. Write and test script locally
2. Create backup copy
3. Encrypt for distribution
4. Test encrypted version
5. Deploy with confidence

## ❓ FAQ

### General Questions

**Q: What types of files can be encrypted?**
A: Primarily bash scripts (.sh files), but the tool can handle any text-based files.

**Q: Is the encryption reversible?**
A: Yes, use the decrypt function to restore original scripts from encrypted versions.

**Q: Can I encrypt already encrypted files?**
A: While possible, it's not recommended as it may cause issues during decryption.

### Technical Questions

**Q: What encryption algorithm is used?**
A: The tool uses bash-obfuscate which employs various obfuscation techniques including variable name mangling and code restructuring.

**Q: Are there file size limitations?**
A: No strict limits, but very large files may take longer to process.

**Q: Can I use this in production environments?**
A: Yes, but always test thoroughly in staging environments first.

### Usage Questions

**Q: How do I batch encrypt multiple files?**
A: Use the file management features or create custom batch scripts using the core functions.

**Q: Can I customize the encryption parameters?**
A: Currently, the tool uses optimized default settings. Custom parameters may be added in future versions.

**Q: What if I forget my encrypted file names?**
A: Use option [3] in the main menu to view all available files with details.

## 📞 Support

Need help? Here are your options:

1. **Check this guide** for common solutions
2. **Review error messages** carefully - they often contain helpful hints
3. **Test with sample scripts** to isolate issues
4. **Check system requirements** and dependencies

## 🔄 Updates

Stay up to date:
- Check the CHANGELOG.md for latest features
- Backup your scripts before updating
- Test new versions with non-critical files first

---

**Happy Encrypting! 🔐**

*UCH-2009 Team*
