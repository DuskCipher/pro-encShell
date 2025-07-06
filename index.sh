
#!/bin/bash

# DuskCipher Pro Toolkit v3.0 - Shell Launcher
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
UNDERLINE='\033[4m'
BLINK='\033[5m'
RESET='\033[0m'

# Status Icons
SUCCESS="${BRIGHT_GREEN}[${WHITE}✓${BRIGHT_GREEN}]${RESET}"
ERROR="${BRIGHT_RED}[${WHITE}✗${BRIGHT_RED}]${RESET}"
WARNING="${BRIGHT_YELLOW}[${WHITE}⚠${BRIGHT_YELLOW}]${RESET}"
INFO="${BRIGHT_CYAN}[${WHITE}ℹ${BRIGHT_CYAN}]${RESET}"
LOADING="${BRIGHT_YELLOW}[${WHITE}⟳${BRIGHT_YELLOW}]${RESET}"
QUESTION="${BRIGHT_BLUE}[${WHITE}?${BRIGHT_BLUE}]${RESET}"

# Animation function
loading_animation() {
    local text="$1"
    local duration="${2:-2}"
    local chars="⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    local i=0
    
    while [ $i -lt $duration ]; do
        for (( j=0; j<${#chars}; j++ )); do
            printf "\r${LOADING} ${WHITE}%s %s${RESET}" "$text" "${chars:$j:1}"
            sleep 0.1
        done
        ((i++))
    done
    printf "\r${SUCCESS} ${WHITE}%s completed!${RESET}\n" "$text"
}

bannerutama() {
# Main banner
echo -e "${MAGENTA}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}║   ${CYAN}██████╗ ██╗   ██╗███████╗██╗  ██╗${YELLOW}     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     ${MAGENTA}║"
echo -e "${MAGENTA}║   ${CYAN}██╔══██╗██║   ██║██╔════╝██║ ██╔╝${YELLOW}    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    ${MAGENTA}║"
echo -e "${MAGENTA}║   ${CYAN}██║  ██║██║   ██║███████╗█████╔╝${YELLOW}     ██║     ██║██████╔╝███████║█████╗  ██████╔╝    ${MAGENTA}║"
echo -e "${MAGENTA}║   ${CYAN}██║  ██║██║   ██║╚════██║██╔═██╗${YELLOW}     ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗    ${MAGENTA}║"
echo -e "${MAGENTA}║   ${CYAN}██████╔╝╚██████╔╝███████║██║  ██╗${YELLOW}    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║    ${MAGENTA}║"
echo -e "${MAGENTA}║   ${CYAN}╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝${YELLOW}     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ${MAGENTA}║"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}║                      ${YELLOW}⚡ PROFESSIONAL ENCRYPTION TOOLKIT v3.0 ⚡${MAGENTA}                       ║"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}║                  ${BRIGHT_RED}🔐 Advanced Script Protection & Obfuscation System 🔐${MAGENTA}                ║"
echo -e "${MAGENTA}║                                                                                       ║"
echo -e "${MAGENTA}╠═══════════════════════════════════════════════════════════════════════════════════════╣"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Author      ${YELLOW}: ${CYAN}./B7${MAGENTA}                                                                 ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Community   ${YELLOW}: ${CYAN}DuskCipher${MAGENTA}                                                           ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Version     ${YELLOW}: ${CYAN}v3.0 Enhanced Shell Interface${MAGENTA}                                        ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Platform    ${YELLOW}: ${CYAN}$(uname -s) $(uname -m)${MAGENTA}                                                         ║"
echo -e "${MAGENTA}║  ${BRIGHT_GREEN}➤ ${WHITE}Status      ${YELLOW}: ${BRIGHT_GREEN}Active & Ready${MAGENTA}                                                       ║"
echo -e "${MAGENTA}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}" 
bannermenu
}

bannermenu() {
# Loading animation
loading_animation "Initializing toolkit" 1

# System information
echo -e "\n${INFO} ${WHITE}System Information:${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Hostname: ${CYAN}$(hostname)${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Current User: ${CYAN}$(whoami)${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Shell: ${CYAN}$SHELL${RESET}"
echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Date: ${CYAN}$(date '+%Y-%m-%d %H:%M:%S')${RESET}"

# Check for available files
echo -e "\n${INFO} ${WHITE}Scanning for user files...${RESET}"
user_files=($(find . -maxdepth 1 -name "*.sh" -not -name "install.sh" -not -name "index.sh" -not -name "main.py" 2>/dev/null))

if [ ${#user_files[@]} -gt 0 ]; then
    echo -e "${SUCCESS} ${WHITE}Found ${CYAN}${#user_files[@]}${WHITE} user script(s):${RESET}"
    for file in "${user_files[@]:0:5}"; do
        size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null || echo "0")
        echo -e "${BRIGHT_GREEN}   ➤ ${CYAN}$(basename "$file")${WHITE} (${size} bytes)${RESET}"
    done
    if [ ${#user_files[@]} -gt 5 ]; then
        echo -e "${BRIGHT_GREEN}   ➤ ${DIM}... and ${CYAN}$((${#user_files[@]} - 5))${WHITE} more files${RESET}"
    fi
else
    echo -e "${WARNING} ${WHITE}No user scripts found. You can create some using the tools below.${RESET}"
fi

# Enhanced main menu
echo -e "\n${BRIGHT_BLUE}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo -e "${BRIGHT_BLUE}║                            🛡️  SHELL INTERFACE MENU  🛡️                                 ║"
echo -e "${BRIGHT_BLUE}╠═══════════════════════════════════════════════════════════════════════════════════════╣"
echo -e "${BRIGHT_BLUE}║                                                                                       ║"
echo -e "${BRIGHT_BLUE}║    ${BRIGHT_WHITE}[${BRIGHT_RED}1${BRIGHT_WHITE}] ${CYAN}🐍 PYTHON INTERFACE${WHITE}    - Launch advanced Python toolkit                        ${BRIGHT_BLUE}║"
echo -e "${BRIGHT_BLUE}║    ${BRIGHT_WHITE}[${BRIGHT_RED}2${BRIGHT_WHITE}] ${CYAN}📝 CREATE SCRIPT${WHITE}       - Create new bash script                                ${BRIGHT_BLUE}║"
echo -e "${BRIGHT_BLUE}║    ${BRIGHT_WHITE}[${BRIGHT_RED}3${BRIGHT_WHITE}] ${CYAN}📁 FILE BROWSER${WHITE}        - Browse and manage files                               ${BRIGHT_BLUE}║"
echo -e "${BRIGHT_BLUE}║    ${BRIGHT_WHITE}[${BRIGHT_RED}4${BRIGHT_WHITE}] ${CYAN}🔧 QUICK ENCRYPT${WHITE}       - Fast encryption (bash-only)                           ${BRIGHT_BLUE}║"
echo -e "${BRIGHT_BLUE}║    ${BRIGHT_WHITE}[${BRIGHT_RED}5${BRIGHT_WHITE}] ${CYAN}🛠️  SYSTEM INFO${WHITE}         - Display system information                            ${BRIGHT_BLUE}║"
echo -e "${BRIGHT_BLUE}║    ${BRIGHT_WHITE}[${BRIGHT_RED}6${BRIGHT_WHITE}] ${CYAN}⚙️  SETUP TOOLS${WHITE}         - Install/update dependencies                           ${BRIGHT_BLUE}║"
echo -e "${BRIGHT_BLUE}║    ${BRIGHT_WHITE}[${BRIGHT_RED}0${BRIGHT_WHITE}] ${CYAN}🚪 EXIT${WHITE}                - Close shell interface                                 ${BRIGHT_BLUE}║"
echo -e "${BRIGHT_BLUE}║                                                                                       ║"
echo -e "${BRIGHT_BLUE}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"
}

# Function to show detailed file information
show_file_details() {
    echo -e "\n${BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
    echo -e "${BRIGHT_CYAN}║                              📁 FILE BROWSER                                          ║"
    echo -e "${BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"
    
    echo -e "\n${INFO} ${WHITE}Available Files:${RESET}"
    
    # Show different file types
    local file_count=0
    
    # Shell scripts
    for file in *.sh; do
        if [ -f "$file" ] && [ "$file" != "install.sh" ] && [ "$file" != "index.sh" ]; then
            size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null || echo "0")
            modified=$(stat -c%y "$file" 2>/dev/null | cut -d. -f1 || stat -f%Sm "$file" 2>/dev/null || echo "unknown")
            echo -e "${BRIGHT_GREEN}   🔧 ${CYAN}$(printf "%-25s" "$file")${WHITE} ${size} bytes ${DIM}(${modified})${RESET}"
            ((file_count++))
        fi
    done
    
    # Python files
    for file in *.py; do
        if [ -f "$file" ] && [ "$file" != "main.py" ]; then
            size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null || echo "0")
            modified=$(stat -c%y "$file" 2>/dev/null | cut -d. -f1 || stat -f%Sm "$file" 2>/dev/null || echo "unknown")
            echo -e "${BRIGHT_YELLOW}   🐍 ${CYAN}$(printf "%-25s" "$file")${WHITE} ${size} bytes ${DIM}(${modified})${RESET}"
            ((file_count++))
        fi
    done
    
    # Other files
    for file in *.txt *.md *.json; do
        if [ -f "$file" ] && [ "$file" != "README.md" ]; then
            size=$(stat -c%s "$file" 2>/dev/null || stat -f%z "$file" 2>/dev/null || echo "0")
            modified=$(stat -c%y "$file" 2>/dev/null | cut -d. -f1 || stat -f%Sm "$file" 2>/dev/null || echo "unknown")
            echo -e "${BRIGHT_MAGENTA}   📄 ${CYAN}$(printf "%-25s" "$file")${WHITE} ${size} bytes ${DIM}(${modified})${RESET}"
            ((file_count++))
        fi
    done
    
    if [ $file_count -eq 0 ]; then
        echo -e "${WARNING} ${WHITE}No user files found. Create some scripts to get started!${RESET}"
    else
        echo -e "\n${SUCCESS} ${WHITE}Total files found: ${CYAN}$file_count${RESET}"
    fi
}

# Function to create new script
create_script() {
    clear
    echo -e "\n${BRIGHT_GREEN}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
    echo -e "${BRIGHT_GREEN}║                              📝 SCRIPT CREATOR                                        ║"
    echo -e "${BRIGHT_GREEN}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"
    
    echo -e "\n${QUESTION} ${WHITE}Script templates available:${RESET}"
    echo -e "${BRIGHT_WHITE}   [1] ${CYAN}Basic Script${WHITE}     - Simple bash script template${RESET}"
    echo -e "${BRIGHT_WHITE}   [2] ${CYAN}System Monitor${WHITE}   - System information script${RESET}"
    echo -e "${BRIGHT_WHITE}   [3] ${CYAN}File Manager${WHITE}     - File operations script${RESET}"
    echo -e "${BRIGHT_WHITE}   [4] ${CYAN}Network Tool${WHITE}     - Network utilities script${RESET}"
    echo -e "${BRIGHT_WHITE}   [5] ${CYAN}Custom Script${WHITE}    - Empty script for custom code${RESET}"
    echo -e "${BRIGHT_WHITE}   [6] ${CYAN}Interactive Mode${WHITE} - Create script with nano editor${RESET}"
    
    echo -e "\n${BRIGHT_WHITE}┌─[${CYAN}./B7${WHITE}@${CYAN}DuskCipher${WHITE}]"
    echo -ne "└─${BRIGHT_GREEN}Template choice (1-6): ${RESET}"
    read -r template_choice
    
    echo -e "\n${BRIGHT_WHITE}┌─[${CYAN}./B7${WHITE}@${CYAN}DuskCipher${WHITE}]"
    echo -ne "└─${BRIGHT_GREEN}Script name (without .sh): ${RESET}"
    read -r script_name
    
    if [ -z "$script_name" ]; then
        echo -e "\n${ERROR} ${WHITE}Script name cannot be empty!${RESET}"
        echo -e "${INFO} ${WHITE}Press Enter to try again...${RESET}"
        read -r
        return 1
    fi
    
    script_file="${script_name}.sh"
    
    # Check if file already exists
    if [ -f "$script_file" ]; then
        echo -e "\n${WARNING} ${WHITE}File ${CYAN}$script_file${WHITE} already exists!${RESET}"
        echo -e "${QUESTION} ${WHITE}Overwrite? (y/N): ${RESET}"
        read -r overwrite
        if [ "$overwrite" != "y" ] && [ "$overwrite" != "Y" ]; then
            echo -e "${INFO} ${WHITE}Script creation cancelled.${RESET}"
            return 1
        fi
    fi
    
    case $template_choice in
        1)
            loading_animation "Creating basic script" 1
            cat > "$script_file" << 'EOF'
#!/bin/bash
# Basic Script Template
# Created by DuskCipher Pro Toolkit v3.0
# Author: ./B7 | Community: DuskCipher

echo "╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                              📝 BASIC SCRIPT TEMPLATE                                 ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "Script Information:"
echo "➤ Script: $0"
echo "➤ User: $(whoami)"
echo "➤ Date: $(date)"
echo "➤ Directory: $(pwd)"

echo ""
echo "=== Basic Operations ==="
echo "Hello, World from DuskCipher!"
echo "This is a basic script template."

echo ""
echo "=== System Info ==="
echo "Hostname: $(hostname)"
echo "OS: $(uname -s)"
echo "Architecture: $(uname -m)"

echo ""
echo "=== File Listing ==="
echo "Files in current directory:"
ls -la

echo ""
echo "✓ Script completed successfully!"
echo "Created with ❤️ by ./B7 & DuskCipher"
EOF
            ;;
        2)
            loading_animation "Creating system monitor" 1
            cat > "$script_file" << 'EOF'
#!/bin/bash
# System Monitor Script
# Created by DuskCipher Pro Toolkit v3.0
# Author: ./B7 | Community: DuskCipher

echo "╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                              🖥️  SYSTEM MONITOR                                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "=== System Information ==="
echo "➤ Hostname: $(hostname)"
echo "➤ Operating System: $(uname -s)"
echo "➤ Kernel Version: $(uname -r)"
echo "➤ Architecture: $(uname -m)"
echo "➤ Current User: $(whoami)"
echo "➤ System Uptime: $(uptime)"

echo ""
echo "=== Memory Information ==="
if command -v free >/dev/null 2>&1; then
    free -h
else
    echo "Memory information not available"
fi

echo ""
echo "=== Disk Usage ==="
if command -v df >/dev/null 2>&1; then
    df -h
else
    echo "Disk information not available"
fi

echo ""
echo "=== Network Information ==="
if command -v ip >/dev/null 2>&1; then
    ip addr show | grep -E "(inet|UP)" | head -10
elif command -v ifconfig >/dev/null 2>&1; then
    ifconfig | grep -E "(inet|UP)" | head -10
else
    echo "Network information not available"
fi

echo ""
echo "=== Top Processes ==="
if command -v ps >/dev/null 2>&1; then
    ps aux | head -10
else
    echo "Process information not available"
fi

echo ""
echo "✓ System monitoring completed!"
echo "Created with ❤️ by ./B7 & DuskCipher"
EOF
            ;;
        3)
            loading_animation "Creating file manager" 1
            cat > "$script_file" << 'EOF'
#!/bin/bash
# File Manager Script
# Created by DuskCipher Pro Toolkit v3.0
# Author: ./B7 | Community: DuskCipher

echo "╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                              📁 FILE MANAGER                                          ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "=== Current Directory ==="
echo "➤ Current path: $(pwd)"
echo "➤ Total files: $(ls -1 | wc -l)"
echo "➤ Total directories: $(ls -d */ 2>/dev/null | wc -l)"

echo ""
echo "=== Directory Contents ==="
ls -la

echo ""
echo "=== File Operations Menu ==="
echo "[1] List files with details"
echo "[2] Create new directory"
echo "[3] Show file sizes"
echo "[4] Find files by extension"
echo "[5] Show hidden files"

echo ""
echo "=== File Statistics ==="
echo "➤ Shell scripts: $(ls *.sh 2>/dev/null | wc -l)"
echo "➤ Python files: $(ls *.py 2>/dev/null | wc -l)"
echo "➤ Text files: $(ls *.txt 2>/dev/null | wc -l)"
echo "➤ Config files: $(ls *.json *.conf *.cfg 2>/dev/null | wc -l)"

echo ""
echo "✓ File manager ready for customization!"
echo "Created with ❤️ by ./B7 & DuskCipher"
EOF
            ;;
        4)
            loading_animation "Creating network tool" 1
            cat > "$script_file" << 'EOF'
#!/bin/bash
# Network Tool Script
# Created by DuskCipher Pro Toolkit v3.0
# Author: ./B7 | Community: DuskCipher

echo "╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                              🌐 NETWORK UTILITIES                                     ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "=== Network Configuration ==="
if command -v ip >/dev/null 2>&1; then
    echo "➤ Network interfaces:"
    ip addr show | grep -E "(inet|UP)" | head -10
elif command -v ifconfig >/dev/null 2>&1; then
    echo "➤ Network interfaces:"
    ifconfig | grep -E "(inet|UP)" | head -10
else
    echo "Network configuration not available"
fi

echo ""
echo "=== Routing Information ==="
if command -v ip >/dev/null 2>&1; then
    echo "➤ Routing table:"
    ip route
elif command -v route >/dev/null 2>&1; then
    echo "➤ Routing table:"
    route -n
else
    echo "Routing information not available"
fi

echo ""
echo "=== DNS Configuration ==="
if [ -f /etc/resolv.conf ]; then
    echo "➤ DNS servers:"
    cat /etc/resolv.conf | grep nameserver
else
    echo "DNS configuration not available"
fi

echo ""
echo "=== Network Statistics ==="
if command -v netstat >/dev/null 2>&1; then
    echo "➤ Network statistics:"
    netstat -i
else
    echo "Network statistics not available"
fi

echo ""
echo "=== Network Tools Available ==="
echo "[1] Ping test"
echo "[2] Port scan"
echo "[3] Network speed test"
echo "[4] DNS lookup"
echo "[5] Traceroute"

echo ""
echo "✓ Network tools ready for customization!"
echo "Created with ❤️ by ./B7 & DuskCipher"
EOF
            ;;
        5)
            loading_animation "Creating custom script" 1
            cat > "$script_file" << 'EOF'
#!/bin/bash
# Custom Script Template
# Created by DuskCipher Pro Toolkit v3.0
# Author: ./B7 | Community: DuskCipher

echo "╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                              🎨 CUSTOM SCRIPT                                         ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "=== Script Information ==="
echo "➤ Script: $0"
echo "➤ Started at: $(date)"
echo "➤ User: $(whoami)"
echo "➤ Directory: $(pwd)"

echo ""
echo "=== Custom Code Section ==="
echo "This is your custom script template."
echo "Add your own functionality below:"

# ═══════════════════════════════════════════════════════════════════════════════════════
# YOUR CUSTOM CODE GOES HERE
# ═══════════════════════════════════════════════════════════════════════════════════════

echo "Hello from your custom script!"
echo "Ready for your awesome code!"

# Example function
custom_function() {
    echo "This is a custom function!"
    echo "You can add your own logic here."
}

# Call the function
custom_function

# ═══════════════════════════════════════════════════════════════════════════════════════
# END OF CUSTOM CODE SECTION
# ═══════════════════════════════════════════════════════════════════════════════════════

echo ""
echo "✓ Custom script completed at: $(date)"
echo "Created with ❤️ by ./B7 & DuskCipher"
EOF
            ;;
        6)
            loading_animation "Preparing interactive mode" 1
            cat > "$script_file" << 'EOF'
#!/bin/bash
# Interactive Script
# Created by DuskCipher Pro Toolkit v3.0
# Author: ./B7 | Community: DuskCipher

echo "╔═══════════════════════════════════════════════════════════════════════════════════════╗"
echo "║                              ⚡ INTERACTIVE SCRIPT                                     ║"
echo "╚═══════════════════════════════════════════════════════════════════════════════════════╝"

echo ""
echo "=== Interactive Script Template ==="
echo "This script will be opened in nano editor for custom editing."
echo "Add your own code after this section."

echo ""
echo "Script created at: $(date)"
echo "Ready for customization!"

# Add your interactive code here

EOF
            chmod +x "$script_file"
            echo -e "\n${SUCCESS} ${WHITE}Script created: ${CYAN}$script_file${RESET}"
            echo -e "${INFO} ${WHITE}Opening in nano editor for customization...${RESET}"
            echo -e "${BRIGHT_YELLOW}┌─ Tips for nano editor:${RESET}"
            echo -e "${BRIGHT_YELLOW}│  Ctrl+O - Save file${RESET}"
            echo -e "${BRIGHT_YELLOW}│  Ctrl+X - Exit editor${RESET}"
            echo -e "${BRIGHT_YELLOW}│  Ctrl+G - Help${RESET}"
            echo -e "${BRIGHT_YELLOW}└─ Press Enter to continue...${RESET}"
            read -r
            nano "$script_file"
            return 0
            ;;
        *)
            echo -e "\n${ERROR} ${WHITE}Invalid template selection!${RESET}"
            echo -e "${INFO} ${WHITE}Please select 1-6${RESET}"
            return 1
            ;;
    esac
    
    chmod +x "$script_file"
    echo -e "\n${SUCCESS} ${WHITE}Script created successfully: ${CYAN}$script_file${RESET}"
    echo -e "${INFO} ${WHITE}File size: ${CYAN}$(stat -c%s "$script_file" 2>/dev/null || stat -f%z "$script_file" 2>/dev/null || echo "unknown") bytes${RESET}"
    echo -e "${INFO} ${WHITE}You can now:${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Edit with: ${CYAN}nano $script_file${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Run with: ${CYAN}bash $script_file${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Encrypt with: ${CYAN}Quick Encrypt menu${RESET}"
    
    echo -e "\n${QUESTION} ${WHITE}Would you like to edit the script now? (y/N): ${RESET}"
    read -r edit_choice
    if [ "$edit_choice" = "y" ] || [ "$edit_choice" = "Y" ]; then
        nano "$script_file"
    fi
}

# Function to show system information
show_system_info() {
    echo -e "\n${BRIGHT_YELLOW}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
    echo -e "${BRIGHT_YELLOW}║                              🖥️  SYSTEM INFORMATION                                    ║"
    echo -e "${BRIGHT_YELLOW}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"
    
    echo -e "\n${INFO} ${WHITE}Hardware Information:${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Hostname: ${CYAN}$(hostname)${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Architecture: ${CYAN}$(uname -m)${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Processor: ${CYAN}$(uname -p 2>/dev/null || echo "unknown")${RESET}"
    
    echo -e "\n${INFO} ${WHITE}Operating System:${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}OS: ${CYAN}$(uname -s)${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Kernel: ${CYAN}$(uname -r)${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Version: ${CYAN}$(uname -v | cut -d' ' -f1-3)${RESET}"
    
    echo -e "\n${INFO} ${WHITE}User Information:${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Current User: ${CYAN}$(whoami)${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Home Directory: ${CYAN}$HOME${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Shell: ${CYAN}$SHELL${RESET}"
    
    echo -e "\n${INFO} ${WHITE}System Status:${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Uptime: ${CYAN}$(uptime | cut -d',' -f1-2)${RESET}"
    echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Load Average: ${CYAN}$(uptime | awk -F'load average:' '{print $2}' | xargs)${RESET}"
    
    # Memory information
    if command -v free >/dev/null 2>&1; then
        echo -e "\n${INFO} ${WHITE}Memory Usage:${RESET}"
        free -h | while read -r line; do
            echo -e "${BRIGHT_GREEN}   ➤ ${CYAN}$line${RESET}"
        done
    fi
    
    # Disk usage
    if command -v df >/dev/null 2>&1; then
        echo -e "\n${INFO} ${WHITE}Disk Usage:${RESET}"
        df -h | head -5 | while read -r line; do
            echo -e "${BRIGHT_GREEN}   ➤ ${CYAN}$line${RESET}"
        done
    fi
}

# Function for quick encryption
quick_encrypt() {
    echo -e "\n${BRIGHT_RED}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
    echo -e "${BRIGHT_RED}║                              🔒 QUICK ENCRYPT                                         ║"
    echo -e "${BRIGHT_RED}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"
    
    # List available scripts
    local scripts=($(find . -maxdepth 1 -name "*.sh" -not -name "install.sh" -not -name "index.sh" 2>/dev/null))
    
    if [ ${#scripts[@]} -eq 0 ]; then
        echo -e "${ERROR} ${WHITE}No scripts found for encryption!${RESET}"
        echo -e "${INFO} ${WHITE}Create a script first using option [2]${RESET}"
        return 1
    fi
    
    echo -e "\n${INFO} ${WHITE}Available scripts for encryption:${RESET}"
    for i in "${!scripts[@]}"; do
        script_name=$(basename "${scripts[$i]}")
        size=$(stat -c%s "${scripts[$i]}" 2>/dev/null || stat -f%z "${scripts[$i]}" 2>/dev/null || echo "0")
        echo -e "${BRIGHT_GREEN}   [$((i+1))] ${CYAN}$script_name${WHITE} (${size} bytes)${RESET}"
    done
    
    echo -ne "\n${QUESTION} ${WHITE}Select script number (1-${#scripts[@]}): ${RESET}"
    read -r script_choice
    
    if ! [[ "$script_choice" =~ ^[0-9]+$ ]] || [ "$script_choice" -lt 1 ] || [ "$script_choice" -gt ${#scripts[@]} ]; then
        echo -e "${ERROR} ${WHITE}Invalid selection!${RESET}"
        return 1
    fi
    
    selected_script="${scripts[$((script_choice-1))]}"
    script_basename=$(basename "$selected_script" .sh)
    encrypted_script="${script_basename}_encrypted.sh"
    
    echo -e "\n${QUESTION} ${WHITE}Output filename (default: $encrypted_script): ${RESET}"
    read -r output_name
    
    if [ -n "$output_name" ]; then
        encrypted_script="$output_name"
    fi
    
    echo -e "\n${LOADING} ${WHITE}Encrypting script...${RESET}"
    
    # Simple base64 encryption for quick mode
    if command -v base64 >/dev/null 2>&1; then
        {
            echo '#!/bin/bash'
            echo '# DuskCipher Pro - Encrypted Script'
            echo '# This script has been encrypted for protection'
            echo ''
            echo 'encrypted_data="'
            base64 -w 0 "$selected_script"
            echo '"'
            echo ''
            echo 'echo "$encrypted_data" | base64 -d | bash'
        } > "$encrypted_script"
        
        chmod +x "$encrypted_script"
        echo -e "\n${SUCCESS} ${WHITE}Quick encryption completed!${RESET}"
        echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Original: ${CYAN}$(basename "$selected_script")${RESET}"
        echo -e "${BRIGHT_GREEN}   ➤ ${WHITE}Encrypted: ${CYAN}$encrypted_script${RESET}"
        echo -e "${INFO} ${WHITE}Test the encrypted script before deployment!${RESET}"
    else
        echo -e "${ERROR} ${WHITE}base64 command not found! Cannot perform quick encryption.${RESET}"
        return 1
    fi
}

# Main menu loop
while true; do
clear
bannerutama
    echo -e "\n${BRIGHT_WHITE}┌─[${CYAN}./B7${WHITE}@${CYAN}DuskCipher${WHITE}]"
    echo -ne "└─${BRIGHT_GREEN}$ ${RESET}" 
           read -r choice
    
    case $choice in
        1)
            echo -e "\n${LOADING} ${WHITE}Launching Python interface...${RESET}"
            sleep 1
            if [ -f "main.py" ]; then
                python3 main.py
            else
                echo -e "${ERROR} ${WHITE}main.py not found! Please run install.sh first.${RESET}"
            fi
            ;;
        2)
            create_script
            ;;
        3)
            show_file_details
            ;;
        4)
            quick_encrypt
            ;;
        5)
            show_system_info
            ;;
        6)
            echo -e "\n${LOADING} ${WHITE}Running setup tools...${RESET}"
            if [ -f "install.sh" ]; then
                bash install.sh
            else
                echo -e "${ERROR} ${WHITE}install.sh not found!${RESET}"
            fi
            ;;
        0|exit|quit)
            echo -e "\n${BRIGHT_GREEN}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
            echo -e "${BRIGHT_GREEN}║                            👋 GOODBYE FROM DUSKCIPHER                                 ║"
            echo -e "${BRIGHT_GREEN}╚═══════════════════════════════════════════════════════════════════════════════════════╝${RESET}"
            echo -e "\n${SUCCESS} ${WHITE}Thank you for using DuskCipher Pro Toolkit!${RESET}"
            echo -e "${BRIGHT_CYAN}🌟 ${WHITE}Stay secure, stay protected! 🌟${RESET}"
            echo -e "${BRIGHT_MAGENTA}Created with ❤️ by ./B7 & DuskCipher Community${RESET}\n"
            exit 0
            ;;
        *)
            echo -e "${ERROR} ${WHITE}Invalid choice! Please select 0-6.${RESET}"
            ;;
    esac
    
    echo -e "\n${DIM}Press Enter to continue...${RESET}"
    read -r
    done