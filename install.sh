
#!/bin/bash

# DuskCipher Pro Toolkit v3.0 - Installation Script
# Advanced Script Protection & Obfuscation System
# Author: ./B7 | Community: DuskCipher

# Enhanced Color System
RED='\033[31m'
GREEN='\033[32m'
YELLOW='\033[33m'
BLUE='\033[34m'
MAGENTA='\033[35m'
CYAN='\033[36m'
WHITE='\033[37m'
BRIGHT_RED='\033[91m'
BRIGHT_GREEN='\033[92m'
BRIGHT_YELLOW='\033[93m'
BRIGHT_BLUE='\033[94m'
BRIGHT_MAGENTA='\033[95m'
BRIGHT_CYAN='\033[96m'
BRIGHT_WHITE='\033[97m'
BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'

# Status Icons
SUCCESS="${BRIGHT_GREEN}[${WHITE}✓${BRIGHT_GREEN}]${RESET}"
ERROR="${BRIGHT_RED}[${WHITE}✗${BRIGHT_RED}]${RESET}"
WARNING="${BRIGHT_YELLOW}[${WHITE}⚠${BRIGHT_YELLOW}]${RESET}"
INFO="${BRIGHT_CYAN}[${WHITE}ℹ${BRIGHT_CYAN}]${RESET}"
LOADING="${BRIGHT_YELLOW}[${WHITE}⟳${BRIGHT_YELLOW}]${RESET}"

# Clear screen
clear

# Installation Banner
echo -e "${MAGENTA}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}║   ${CYAN}██████╗ ██╗   ██╗███████╗██╗  ██╗${YELLOW}     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗  ${MAGENTA}   ║"
echo -e "${MAGENTA}║   ${CYAN}██╔══██╗██║   ██║██╔════╝██║ ██╔╝${YELLOW}    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗ ${MAGENTA}   ║"
echo -e "${MAGENTA}║   ${CYAN}██║  ██║██║   ██║███████╗█████╔╝${YELLOW}     ██║     ██║██████╔╝███████║█████╗  ██████╔╝ ${MAGENTA}   ║"
echo -e "${MAGENTA}║   ${CYAN}██║  ██║██║   ██║╚════██║██╔═██╗${YELLOW}     ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗ ${MAGENTA}   ║"
echo -e "${MAGENTA}║   ${CYAN}██████╔╝╚██████╔╝███████║██║  ██╗${YELLOW}    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║ ${MAGENTA}   ║"
echo -e "${MAGENTA}║   ${CYAN}╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝${YELLOW}     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ${MAGENTA}   ║"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}║              ${YELLOW}⚡ PROFESSIONAL ENCRYPTION TOOLKIT v3.0 ⚡${MAGENTA}                               ║"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}║          ${BRIGHT_RED}🔐 Advanced Script Protection & Obfuscation System 🔐${MAGENTA}                        ║"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}╠═══════════════════════════════════════════════════════════════════════════════════════╣"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Author      ${YELLOW}: ${CYAN}./B7${MAGENTA}                                                                 ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Community   ${YELLOW}: ${CYAN}DuskCipher${MAGENTA}                                                           ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Version     ${YELLOW}: ${CYAN}v3.0 Enhanced${MAGENTA}                                                        ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Platform    ${YELLOW}: ${CYAN}$(uname -s) $(uname -m)${MAGENTA}                                                         ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Status      ${YELLOW}: ${BRIGHT_GREEN}Installing Components${MAGENTA}                                                ║"
echo -e "${MAGENTA}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"

echo ""
echo -e "${BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo -e "${BRIGHT_CYAN}║                              🚀 INSTALLATION PROCESS                                  ║"
echo -e "${BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"

# Loading animation
echo -e "${LOADING} ${WHITE}Initializing installation process..."
sleep 1

# Function to show progress
show_progress() {
    local message="$1"
    local duration="$2"
    echo -e "\n${INFO} ${WHITE}$message${RESET}"
    
    local bar_length=50
    for ((i=0; i<=bar_length; i++)); do
        local percent=$((i * 100 / bar_length))
        local filled=$(printf "█%.0s" $(seq 1 $i))
        local empty=$(printf "░%.0s" $(seq 1 $((bar_length - i))))
        printf "\r${CYAN}[${filled}${empty}] ${percent}%%${RESET}"
        sleep $(echo "scale=3; $duration / $bar_length" | bc -l 2>/dev/null || echo "0.04")
    done
    echo -e "\n${SUCCESS} ${WHITE}$message completed!${RESET}"
}

# System check
echo -e "\n${INFO} ${WHITE}Performing system checks...${RESET}"
sleep 1

# Check for required commands
check_command() {
    local cmd="$1"
    local name="$2"
    
    if command -v "$cmd" >/dev/null 2>&1; then
        echo -e "${SUCCESS} ${WHITE}$name is available${RESET}"
        return 0
    else
        echo -e "${ERROR} ${WHITE}$name is not available${RESET}"
        return 1
    fi
}

# Check system requirements
echo -e "\n${BRIGHT_YELLOW}➤ ${WHITE}Checking system requirements...${RESET}"
check_command "python3" "Python 3"
check_command "bash" "Bash"
check_command "npm" "Node.js/NPM"

# Create directories
echo -e "\n${INFO} ${WHITE}Creating directory structure...${RESET}"
directories=("config" "logs" "backups" "test_scripts")

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo -e "${SUCCESS} ${WHITE}Created directory: ${CYAN}$dir${RESET}"
    else
        echo -e "${INFO} ${WHITE}Directory exists: ${CYAN}$dir${RESET}"
    fi
done

# Install npm dependencies
if command -v npm >/dev/null 2>&1; then
    echo -e "\n${INFO} ${WHITE}Installing npm dependencies...${RESET}"
    
    # Check if package.json exists
    if [ ! -f "package.json" ]; then
        echo -e "${LOADING} ${WHITE}Creating package.json...${RESET}"
        npm init -y >/dev/null 2>&1
        echo -e "${SUCCESS} ${WHITE}Package.json created${RESET}"
    fi
    
    # Install bash-obfuscate
    echo -e "${LOADING} ${WHITE}Installing bash-obfuscate...${RESET}"
    if npm install bash-obfuscate >/dev/null 2>&1; then
        echo -e "${SUCCESS} ${WHITE}bash-obfuscate installed successfully${RESET}"
    else
        echo -e "${WARNING} ${WHITE}bash-obfuscate installation failed, but tool will still work${RESET}"
    fi
else
    echo -e "${WARNING} ${WHITE}NPM not found, some features may be limited${RESET}"
fi

# Create configuration files
echo -e "\n${INFO} ${WHITE}Creating configuration files...${RESET}"

# Create duskcipher.json
cat > config/duskcipher.json << 'EOF'
{
  "version": "3.0",
  "author": "./B7",
  "community": "DuskCipher",
  "theme": "dark",
  "auto_backup": true,
  "encryption_method": "advanced",
  "log_level": "info",
  "created": "2024-01-01T00:00:00.000Z",
  "stats": {
    "files_encrypted": 0,
    "files_decrypted": 0,
    "total_runs": 0
  }
}
EOF

echo -e "${SUCCESS} ${WHITE}Configuration file created${RESET}"

# Create colors.sh
cat > config/colors.sh << 'EOF'
#!/bin/bash
# DuskCipher Pro - Color Definitions

# Basic Colors
export RED='\033[31m'
export GREEN='\033[32m'
export YELLOW='\033[33m'
export BLUE='\033[34m'
export MAGENTA='\033[35m'
export CYAN='\033[36m'
export WHITE='\033[37m'

# Bright Colors
export BRIGHT_RED='\033[91m'
export BRIGHT_GREEN='\033[92m'
export BRIGHT_YELLOW='\033[93m'
export BRIGHT_BLUE='\033[94m'
export BRIGHT_MAGENTA='\033[95m'
export BRIGHT_CYAN='\033[96m'
export BRIGHT_WHITE='\033[97m'

# Text Effects
export BOLD='\033[1m'
export DIM='\033[2m'
export UNDERLINE='\033[4m'
export BLINK='\033[5m'
export RESET='\033[0m'

# Status Icons
export SUCCESS="${BRIGHT_GREEN}[${WHITE}✓${BRIGHT_GREEN}]${RESET}"
export ERROR="${BRIGHT_RED}[${WHITE}✗${BRIGHT_RED}]${RESET}"
export WARNING="${BRIGHT_YELLOW}[${WHITE}⚠${BRIGHT_YELLOW}]${RESET}"
export INFO="${BRIGHT_CYAN}[${WHITE}ℹ${BRIGHT_CYAN}]${RESET}"
export LOADING="${BRIGHT_YELLOW}[${WHITE}⟳${BRIGHT_YELLOW}]${RESET}"
EOF

echo -e "${SUCCESS} ${WHITE}Color definitions created${RESET}"

# Create sample test script
cat > test_scripts/advanced_test.sh << 'EOF'
#!/bin/bash
# DuskCipher Pro - Advanced Test Script
# This script demonstrates various features for encryption testing

echo "=== DuskCipher Pro Test Script ==="
echo "Testing encryption capabilities..."

# System information
echo "System: $(uname -s) $(uname -r)"
echo "User: $(whoami)"
echo "Date: $(date)"

# Sample operations
for i in {1..5}; do
    echo "Processing step $i..."
    sleep 0.5
done

# File operations
echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -la

# Network test
echo "Network interfaces:"
ip addr show 2>/dev/null || ifconfig 2>/dev/null || echo "Network info unavailable"

# Completion
echo "Test completed successfully!"
echo "This script is ready for encryption testing."
EOF

chmod +x test_scripts/advanced_test.sh
echo -e "${SUCCESS} ${WHITE}Sample test script created${RESET}"

# Set permissions
echo -e "\n${INFO} ${WHITE}Setting file permissions...${RESET}"
chmod +x main.py
chmod +x index.sh
chmod +x install.sh
echo -e "${SUCCESS} ${WHITE}File permissions set${RESET}"

# Progress simulation
show_progress "Finalizing installation" 2

# Success message
echo -e "\n${BRIGHT_GREEN}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo -e "${BRIGHT_GREEN}║                           🎉 INSTALLATION COMPLETED! 🎉                               ║"
echo -e "${BRIGHT_GREEN}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"

echo -e "\n${SUCCESS} ${WHITE}DuskCipher Pro Toolkit v3.0 has been installed successfully!${RESET}"
echo -e "\n${BRIGHT_CYAN}🚀 ${WHITE}Getting Started:${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Run: ${CYAN}python3 main.py${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Or:  ${CYAN}bash index.sh${RESET}"
echo -e "\n${BRIGHT_CYAN}📝 ${WHITE}Features Available:${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Advanced script encryption${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Security vulnerability scanner${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Batch file operations${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Comprehensive backup system${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}System monitoring tools${RESET}"
echo -e "\n${BRIGHT_CYAN}🔐 ${WHITE}Security Features:${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Military-grade encryption${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Automatic backup protection${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}File integrity verification${RESET}"
echo -e "\n${BRIGHT_YELLOW}⚠️  ${WHITE}Important Notes:${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Always backup your scripts before encryption${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Test encrypted scripts before deployment${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Keep the original files in a safe location${RESET}"

echo -e "\n${BRIGHT_MAGENTA}╭─────────────────────────────────────────────────────────────────────────────────────╮"
echo -e "${BRIGHT_MAGENTA}│                    Created with ❤️ by ./B7 & DuskCipher                              │"
echo -e "${BRIGHT_MAGENTA}╰─────────────────────────────────────────────────────────────────────────────────────╯${RESET}"

echo -e "\n${BRIGHT_WHITE}🌟 ${WHITE}Installation complete! Launching DuskCipher interface...${RESET}"
sleep 2

echo -e "\n${LOADING} ${WHITE}Starting DuskCipher Pro Toolkit...${RESET}"
sleep 1

echo ""
echo -ne "${YELLOW}Launch interface now? (Y/n): ${NC}"
    read -r launch_choice
    
    if [[ "$launch_choice" =~ ^[Nn]$ ]]; then
        echo -e "${CYAN}You can start DUSK CIPHER anytime with: ${YELLOW}bash index.sh${NC}"
    else
        echo -e "${GREEN}🚀 Launching Tools interface...${NC}"
        echo ""
        bash index.sh
    fi