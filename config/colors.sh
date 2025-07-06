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
