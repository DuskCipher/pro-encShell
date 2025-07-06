#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DuskCipher Professional Encryption Toolkit v3.0
Advanced Script Protection & Obfuscation System
Author: ./B7
Community: DuskCipher
"""

import os
import sys
import time
import json
import hashlib
import subprocess
import platform
from datetime import datetime
from pathlib import Path


# Enhanced Color System
class Colors:
    # Basic Colors
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'

    # Foreground Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright Colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Extended Colors
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[38;5;93m'
    PINK = '\033[38;5;205m'
    LIME = '\033[38;5;118m'
    GOLD = '\033[38;5;220m'
    SILVER = '\033[38;5;7m'


# Initialize colors
c = Colors()


# Status Icons with enhanced styling
class Icons:
    SUCCESS = f"{c.BRIGHT_GREEN}[{c.WHITE}✓{c.BRIGHT_GREEN}]{c.RESET}"
    ERROR = f"{c.BRIGHT_RED}[{c.WHITE}✗{c.BRIGHT_RED}]{c.RESET}"
    WARNING = f"{c.BRIGHT_YELLOW}[{c.WHITE}⚠{c.BRIGHT_YELLOW}]{c.RESET}"
    INFO = f"{c.BRIGHT_CYAN}[{c.WHITE}ℹ{c.BRIGHT_CYAN}]{c.RESET}"
    QUESTION = f"{c.BRIGHT_BLUE}[{c.WHITE}?{c.BRIGHT_BLUE}]{c.RESET}"
    LOADING = f"{c.BRIGHT_YELLOW}[{c.WHITE}⟳{c.BRIGHT_YELLOW}]{c.RESET}"
    PROCESS = f"{c.BRIGHT_MAGENTA}[{c.WHITE}⚙{c.BRIGHT_MAGENTA}]{c.RESET}"
    SECURITY = f"{c.BRIGHT_RED}[{c.WHITE}🔐{c.BRIGHT_RED}]{c.RESET}"
    FOLDER = f"{c.BRIGHT_CYAN}[{c.WHITE}📁{c.BRIGHT_CYAN}]{c.RESET}"
    FILE = f"{c.BRIGHT_WHITE}[{c.WHITE}📄{c.BRIGHT_WHITE}]{c.RESET}"


# System Information
class SystemInfo:

    @staticmethod
    def get_system_info():
        return {
            'os': platform.system(),
            'platform': platform.platform(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': platform.python_version(),
            'hostname': platform.node(),
            'username': os.getenv('USER', 'unknown'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


# Configuration Manager
class ConfigManager:

    def __init__(self):
        self.config_dir = Path('config')
        self.config_file = self.config_dir / 'duskcipher.json'
        self.config_dir.mkdir(exist_ok=True)

    def load_config(self):
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return self.get_default_config()

    def save_config(self, config):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            return True
        except:
            return False

    def get_default_config(self):
        return {
            'version': '3.0',
            'author': './B7',
            'community': 'DuskCipher',
            'theme': 'dark',
            'auto_backup': True,
            'encryption_method': 'advanced',
            'log_level': 'info',
            'created': datetime.now().isoformat(),
            'stats': {
                'files_encrypted': 0,
                'files_decrypted': 0,
                'total_runs': 0
            }
        }


# Logger System
class Logger:

    def __init__(self):
        self.log_dir = Path('logs')
        self.log_dir.mkdir(exist_ok=True)
        self.log_file = self.log_dir / f'duskcipher_{datetime.now().strftime("%Y%m%d")}.log'

    def log(self, level, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'[{timestamp}] [{level.upper()}] {message}\n'

        try:
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
        except:
            pass


# File Manager
class FileManager:

    def __init__(self):
        self.hidden_files = {
            'install.sh', 'index.sh', 'main.py', '.replit', '.gitignore'
        }
        self.backup_dir = Path('backups')
        self.backup_dir.mkdir(exist_ok=True)

    def get_user_files(self, extension=None):
        files = []
        for file_path in Path('.').glob('*'):
            if file_path.is_file() and file_path.name not in self.hidden_files:
                if extension is None or file_path.suffix == extension:
                    files.append(file_path)
        return sorted(files)

    def get_file_info(self, filepath):
        try:
            stat = filepath.stat()
            return {
                'name':
                filepath.name,
                'size':
                stat.st_size,
                'modified':
                datetime.fromtimestamp(
                    stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'permissions':
                oct(stat.st_mode)[-3:],
                'hash':
                self.get_file_hash(filepath)
            }
        except:
            return None

    def get_file_hash(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()[:16]
        except:
            return 'unknown'

    def backup_file(self, filepath):
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"{filepath.stem}_{timestamp}{filepath.suffix}"
            backup_path = self.backup_dir / backup_name

            with open(filepath, 'rb') as src, open(backup_path, 'wb') as dst:
                dst.write(src.read())

            return backup_path
        except:
            return None


# Animation System
class Animations:

    @staticmethod
    def typewriter(text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def loading_bar(message, duration=2):
        print(f"\n{Icons.LOADING} {message}")
        bar_length = 50
        for i in range(bar_length + 1):
            percent = (i / bar_length) * 100
            filled = '█' * i
            empty = '░' * (bar_length - i)
            print(f"\r{c.CYAN}[{filled}{empty}] {percent:.1f}%{c.RESET}",
                  end='',
                  flush=True)
            time.sleep(duration / bar_length)
        print(f"\n{Icons.SUCCESS} {message} completed!")

    @staticmethod
    def spinner(message, duration=2):
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            frame = frames[i % len(frames)]
            print(f"\r{Icons.LOADING} {message} {c.YELLOW}{frame}{c.RESET}",
                  end='',
                  flush=True)
            time.sleep(0.1)
            i += 1
        print(f"\r{Icons.SUCCESS} {message} completed!{' ' * 10}")


# Main Application Class
class DuskCipherPro:

    def __init__(self):
        self.config_manager = ConfigManager()
        self.config = self.config_manager.load_config()
        self.logger = Logger()
        self.file_manager = FileManager()
        self.system_info = SystemInfo.get_system_info()

        # Update stats
        self.config['stats']['total_runs'] += 1
        self.config_manager.save_config(self.config)

        self.logger.log('info', 'DuskCipher Pro initialized')

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_banner(self):
        banner = f"""
{c.PURPLE}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.PURPLE}║                                                                                       ║
{c.PURPLE}║   {c.CYAN}██████╗ ██╗   ██╗███████╗██╗  ██╗{c.GOLD}     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗  {c.PURPLE}   ║
{c.PURPLE}║   {c.CYAN}██╔══██╗██║   ██║██╔════╝██║ ██╔╝{c.GOLD}    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗ {c.PURPLE}   ║
{c.PURPLE}║   {c.CYAN}██║  ██║██║   ██║███████╗█████╔╝{c.GOLD}     ██║     ██║██████╔╝███████║█████╗  ██████╔╝ {c.PURPLE}   ║
{c.PURPLE}║   {c.CYAN}██║  ██║██║   ██║╚════██║██╔═██╗{c.GOLD}     ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗ {c.PURPLE}   ║
{c.PURPLE}║   {c.CYAN}██████╔╝╚██████╔╝███████║██║  ██╗{c.GOLD}    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║ {c.PURPLE}   ║
{c.PURPLE}║   {c.CYAN}╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝{c.GOLD}     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ {c.PURPLE}   ║
{c.PURPLE}║                                                                                       ║
{c.PURPLE}║              {c.GOLD}⚡ PROFESSIONAL ENCRYPTION TOOLKIT v3.0 ⚡{c.PURPLE}                               ║
{c.PURPLE}║                                                                                       ║
{c.PURPLE}║          {c.ORANGE}🔐 Advanced Script Protection & Obfuscation System 🔐{c.PURPLE}                        ║
{c.PURPLE}║                                                                                       ║
{c.PURPLE}╠═══════════════════════════════════════════════════════════════════════════════════════╣
{c.PURPLE}║  {c.BRIGHT_GREEN}➤ {c.WHITE}Author      {c.YELLOW}: {c.CYAN}{self.config['author']}{c.PURPLE}                                                                 ║
{c.PURPLE}║  {c.BRIGHT_GREEN}➤ {c.WHITE}Community   {c.YELLOW}: {c.CYAN}{self.config['community']}{c.PURPLE}                                                           ║
{c.PURPLE}║  {c.BRIGHT_GREEN}➤ {c.WHITE}Version     {c.YELLOW}: {c.CYAN}v{self.config['version']} Enhanced{c.PURPLE}                                                        ║
{c.PURPLE}║  {c.BRIGHT_GREEN}➤ {c.WHITE}Platform    {c.YELLOW}: {c.CYAN}{self.system_info['os']} {self.system_info['machine']}{c.PURPLE}                                                         ║
{c.PURPLE}║  {c.BRIGHT_GREEN}➤ {c.WHITE}Total Runs  {c.YELLOW}: {c.CYAN}{self.config['stats']['total_runs']}{c.PURPLE}                                                                   ║   
{c.PURPLE}║  {c.BRIGHT_GREEN}➤ {c.WHITE}Status      {c.YELLOW}: {c.BRIGHT_GREEN}Active & Secure{c.PURPLE}                                                      ║    
{c.PURPLE}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
"""
        print(banner)

    def display_main_menu(self):
        files = self.file_manager.get_user_files()
        file_count = len(files)

        menu = f"""
{c.GOLD}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.GOLD}║                            🛡️  ENCRYPTION OPERATIONS  🛡️                                ║
{c.GOLD}╠═══════════════════════════════════════════════════════════════════════════════════════╣
{c.GOLD}║                                                                                       ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}1{c.BRIGHT_BLUE}] {c.CYAN}🔒 ENCRYPT SCRIPT{c.WHITE}      - Protect your bash files            {c.GOLD}                   ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}2{c.BRIGHT_BLUE}] {c.CYAN}🔓 DECRYPT SCRIPT{c.WHITE}      - Restore original files            {c.GOLD}                    ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}3{c.BRIGHT_BLUE}] {c.CYAN}📊 FILE ANALYZER{c.WHITE}       - Advanced file analysis            {c.GOLD}                    ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}4{c.BRIGHT_BLUE}] {c.CYAN}🛠️  BATCH OPERATIONS{c.WHITE}   - Multiple file processing          {c.GOLD}                     ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}5{c.BRIGHT_BLUE}] {c.CYAN}🔍 SECURITY SCANNER{c.WHITE}    - Vulnerability assessment          {c.GOLD}                    ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}6{c.BRIGHT_BLUE}] {c.CYAN}📈 STATISTICS{c.WHITE}          - Usage statistics & reports        {c.GOLD}                    ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}7{c.BRIGHT_BLUE}] {c.CYAN}⚙️  SYSTEM TOOLS{c.WHITE}        - Advanced system utilities         {c.GOLD}                    ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}8{c.BRIGHT_BLUE}] {c.CYAN}🎨 CUSTOMIZATION{c.WHITE}       - Themes & preferences              {c.GOLD}                    ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}9{c.BRIGHT_BLUE}] {c.CYAN}💾 BACKUP MANAGER{c.WHITE}      - Backup & restore operations       {c.GOLD}                    ║
{c.GOLD}║    {c.BRIGHT_BLUE}[{c.BRIGHT_RED}0{c.BRIGHT_BLUE}] {c.CYAN}🚪 EXIT TOOLS{c.WHITE}          - Close application                 {c.GOLD}                    ║
{c.GOLD}║                                                                                       ║
{c.GOLD}║  {c.BRIGHT_CYAN}📁 Files Available: {c.WHITE}{file_count}{c.GOLD}                                                                ║
{c.GOLD}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
"""
        print(menu)

        if file_count > 0:
            print(
                f"{Icons.SUCCESS} {c.WHITE}User files detected: {c.CYAN}{', '.join([f.name for f in files[:3]])}{c.WHITE}{'...' if file_count > 3 else ''}{c.RESET}"
            )
        else:
            print(
                f"{Icons.WARNING} {c.WHITE}No user scripts found. Create some scripts first!{c.RESET}"
            )

    def file_analyzer(self):
        self.clear_screen()
        print(f"""
{c.CYAN}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.CYAN}║                              📊 ADVANCED FILE ANALYZER                               ║
{c.CYAN}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        files = self.file_manager.get_user_files()

        if not files:
            print(
                f"{Icons.WARNING} {c.WHITE}No user files found to analyze.{c.RESET}"
            )
            input(
                f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}"
            )
            return

        print(
            f"{Icons.INFO} {c.WHITE}Analyzing {c.CYAN}{len(files)}{c.WHITE} files...\n{c.RESET}"
        )

        total_size = 0
        file_types = {}

        for i, file_path in enumerate(files, 1):
            file_info = self.file_manager.get_file_info(file_path)
            if file_info:
                total_size += file_info['size']
                ext = file_path.suffix.lower()
                file_types[ext] = file_types.get(ext, 0) + 1

                status = "🟢 Good" if file_info['size'] > 0 else "🔴 Empty"

                print(
                    f"{c.BRIGHT_WHITE}[{i:2d}] {c.CYAN}{file_info['name']:<20}{c.RESET}"
                )
                print(
                    f"     {c.BRIGHT_BLACK}├─ Size: {c.WHITE}{file_info['size']} bytes{c.RESET}"
                )
                print(
                    f"     {c.BRIGHT_BLACK}├─ Modified: {c.WHITE}{file_info['modified']}{c.RESET}"
                )
                print(
                    f"     {c.BRIGHT_BLACK}├─ Permissions: {c.WHITE}{file_info['permissions']}{c.RESET}"
                )
                print(
                    f"     {c.BRIGHT_BLACK}├─ Hash: {c.WHITE}{file_info['hash']}{c.RESET}"
                )
                print(f"     {c.BRIGHT_BLACK}└─ Status: {status}{c.RESET}")
                print()

        print(
            f"{c.GOLD}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            f"{c.GOLD}║                                    SUMMARY                                            ║"
        )
        print(
            f"{c.GOLD}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}"
        )
        print(
            f"{c.BRIGHT_GREEN}➤ {c.WHITE}Total Files: {c.CYAN}{len(files)}{c.RESET}"
        )
        print(
            f"{c.BRIGHT_GREEN}➤ {c.WHITE}Total Size: {c.CYAN}{total_size} bytes ({total_size/1024:.2f} KB){c.RESET}"
        )
        print(
            f"{c.BRIGHT_GREEN}➤ {c.WHITE}File Types: {c.CYAN}{', '.join([f'{ext}({count})' for ext, count in file_types.items()])}{c.RESET}"
        )

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def encrypt_script(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_RED}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_RED}║                                🔒 ENCRYPT MODE                                        ║
{c.BRIGHT_RED}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        files = self.file_manager.get_user_files('.sh')

        if not files:
            print(
                f"{Icons.ERROR} {c.WHITE}No .sh files found to encrypt!{c.RESET}"
            )
            input(
                f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}"
            )
            return

        print(
            f"{Icons.INFO} {c.WHITE}Available files for encryption:{c.RESET}")
        for i, file_path in enumerate(files, 1):
            file_info = self.file_manager.get_file_info(file_path)
            print(
                f"  {c.BRIGHT_WHITE}[{i}] {c.CYAN}{file_path.name}{c.WHITE} ({file_info['size']} bytes){c.RESET}"
            )

        try:
            choice = input(
                f"\n{Icons.QUESTION} {c.WHITE}Select file number or enter filename: {c.RESET}"
            )

            if choice.isdigit():
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    script_path = files[file_index]
                else:
                    print(
                        f"{Icons.ERROR} {c.WHITE}Invalid file number!{c.RESET}"
                    )
                    return
            else:
                script_path = Path(choice)
                if not script_path.exists():
                    print(
                        f"{Icons.ERROR} {c.WHITE}File '{choice}' not found!{c.RESET}"
                    )
                    return

            output_name = input(
                f"{Icons.QUESTION} {c.WHITE}Enter output filename (or press Enter for auto): {c.RESET}"
            )
            if not output_name:
                output_name = f"{script_path.stem}_encrypted{script_path.suffix}"

            # Backup original file
            backup_path = self.file_manager.backup_file(script_path)
            if backup_path:
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Backup created: {c.CYAN}{backup_path.name}{c.RESET}"
                )

            Animations.loading_bar("Initializing encryption", 1)

            # Check for encryption tools
            if not self.check_encryption_tools():
                return

            Animations.loading_bar("Encrypting script", 3)

            # Perform encryption
            success = self.perform_encryption(script_path, output_name)

            if success:
                print(
                    f"{Icons.SUCCESS} {c.BRIGHT_GREEN}Encryption completed successfully!{c.RESET}"
                )
                print(
                    f"{c.BRIGHT_GREEN}➤{c.WHITE} Original: {c.CYAN}{script_path.name}{c.RESET}"
                )
                print(
                    f"{c.BRIGHT_GREEN}➤{c.WHITE} Encrypted: {c.CYAN}{output_name}{c.RESET}"
                )

                # Update stats
                self.config['stats']['files_encrypted'] += 1
                self.config_manager.save_config(self.config)

                self.logger.log(
                    'info',
                    f'File encrypted: {script_path.name} -> {output_name}')
            else:
                print(
                    f"{Icons.ERROR} {c.BRIGHT_RED}Encryption failed!{c.RESET}")

        except KeyboardInterrupt:
            print(
                f"\n{Icons.ERROR} {c.WHITE}Operation cancelled by user!{c.RESET}"
            )
        except Exception as e:
            print(f"{Icons.ERROR} {c.WHITE}Error: {str(e)}{c.RESET}")

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def decrypt_script(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_CYAN}║                                🔓 DECRYPT MODE                                        ║
{c.BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        files = self.file_manager.get_user_files('.sh')

        if not files:
            print(
                f"{Icons.ERROR} {c.WHITE}No .sh files found to decrypt!{c.RESET}"
            )
            input(
                f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}"
            )
            return

        print(
            f"{Icons.INFO} {c.WHITE}Available files for decryption:{c.RESET}")
        for i, file_path in enumerate(files, 1):
            file_info = self.file_manager.get_file_info(file_path)
            print(
                f"  {c.BRIGHT_WHITE}[{i}] {c.CYAN}{file_path.name}{c.WHITE} ({file_info['size']} bytes){c.RESET}"
            )

        try:
            script_name = input(
                f"\n{Icons.QUESTION} {c.WHITE}Enter encrypted script name: {c.RESET}"
            )

            if not os.path.exists(script_name):
                print(
                    f"{Icons.ERROR} {c.WHITE}File '{script_name}' not found!{c.RESET}"
                )
                return

            output_name = input(
                f"{Icons.QUESTION} {c.WHITE}Enter output filename: {c.RESET}")

            Animations.loading_bar("Reading encrypted file", 1)

            with open(script_name, 'r') as f:
                filedata = f.read()

            newdata = filedata.replace("eval", "echo")

            Animations.loading_bar("Decrypting script", 2)

            with open(output_name, 'w') as f:
                f.write(newdata)

            # Process the decryption
            os.system("touch temp_decrypt.sh")
            os.system(f"bash {output_name} > temp_decrypt.sh")
            os.remove(output_name)
            os.system(f"mv temp_decrypt.sh {output_name}")

            print(
                f"{Icons.SUCCESS} {c.BRIGHT_GREEN}Decryption completed successfully!{c.RESET}"
            )
            print(
                f"{c.BRIGHT_GREEN}➤{c.WHITE} Output file: {c.CYAN}{output_name}{c.RESET}"
            )

            # Update stats
            self.config['stats']['files_decrypted'] += 1
            self.config_manager.save_config(self.config)

            self.logger.log('info',
                            f'File decrypted: {script_name} -> {output_name}')

        except KeyboardInterrupt:
            print(
                f"\n{Icons.ERROR} {c.WHITE}Operation cancelled by user!{c.RESET}"
            )
        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Decryption failed: {str(e)}{c.RESET}")

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def check_encryption_tools(self):
        """Check if encryption tools are available"""
        try:
            # Check for bash-obfuscate
            result = subprocess.run(['which', 'bash-obfuscate'],
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                return True

            # Check for local node_modules
            if os.path.exists("node_modules/.bin/bash-obfuscate"):
                return True

            # Install if not found
            print(
                f"{Icons.LOADING} {c.WHITE}Installing bash-obfuscate...{c.RESET}"
            )

            # Initialize npm if needed
            if not os.path.exists("package.json"):
                subprocess.run(['npm', 'init', '-y'], capture_output=True)

            # Install bash-obfuscate
            result = subprocess.run(['npm', 'install', 'bash-obfuscate'],
                                    capture_output=True,
                                    text=True)

            if result.returncode == 0:
                print(
                    f"{Icons.SUCCESS} {c.WHITE}bash-obfuscate installed successfully!{c.RESET}"
                )
                return True
            else:
                print(
                    f"{Icons.ERROR} {c.WHITE}Failed to install bash-obfuscate!{c.RESET}"
                )
                return False

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Error checking encryption tools: {str(e)}{c.RESET}"
            )
            return False

    def perform_encryption(self, script_path, output_name):
        """Perform the actual encryption"""
        try:
            if os.path.exists("node_modules/.bin/bash-obfuscate"):
                cmd = f"./node_modules/.bin/bash-obfuscate {script_path} -o {output_name}"
            else:
                cmd = f"bash-obfuscate {script_path} -o {output_name}"

            result = subprocess.run(cmd,
                                    shell=True,
                                    capture_output=True,
                                    text=True)
            return result.returncode == 0

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Encryption error: {str(e)}{c.RESET}")
            return False

    def batch_operations(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_MAGENTA}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_MAGENTA}║                              🛠️  BATCH OPERATIONS                                      ║
{c.BRIGHT_MAGENTA}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        files = self.file_manager.get_user_files('.sh')

        if not files:
            print(
                f"{Icons.ERROR} {c.WHITE}No .sh files found for batch operations!{c.RESET}"
            )
            input(
                f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}"
            )
            return

        print(f"{Icons.INFO} {c.WHITE}Available batch operations:{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[1] {c.CYAN}Encrypt All Files{c.RESET}")
        print(
            f"  {c.BRIGHT_WHITE}[2] {c.CYAN}Create Backup of All Files{c.RESET}"
        )
        print(f"  {c.BRIGHT_WHITE}[3] {c.CYAN}Generate File Reports{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[4] {c.CYAN}Verify File Integrity{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[0] {c.CYAN}Back to Main Menu{c.RESET}")

        try:
            choice = input(
                f"\n{Icons.QUESTION} {c.WHITE}Select batch operation: {c.RESET}"
            )

            if choice == '1':
                self.batch_encrypt_all(files)
            elif choice == '2':
                self.batch_backup_all(files)
            elif choice == '3':
                self.generate_file_reports(files)
            elif choice == '4':
                self.verify_file_integrity(files)
            elif choice == '0':
                return
            else:
                print(f"{Icons.ERROR} {c.WHITE}Invalid choice!{c.RESET}")

        except KeyboardInterrupt:
            print(
                f"\n{Icons.ERROR} {c.WHITE}Operation cancelled by user!{c.RESET}"
            )

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def batch_encrypt_all(self, files):
        """Encrypt all files in batch"""
        print(
            f"\n{Icons.INFO} {c.WHITE}Starting batch encryption for {len(files)} files...{c.RESET}"
        )

        if not self.check_encryption_tools():
            return

        success_count = 0
        for i, file_path in enumerate(files, 1):
            print(
                f"\n{Icons.PROCESS} {c.WHITE}Processing file {i}/{len(files)}: {c.CYAN}{file_path.name}{c.RESET}"
            )

            output_name = f"{file_path.stem}_encrypted{file_path.suffix}"

            if self.perform_encryption(file_path, output_name):
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Encrypted: {c.CYAN}{output_name}{c.RESET}"
                )
                success_count += 1
            else:
                print(
                    f"{Icons.ERROR} {c.WHITE}Failed to encrypt: {c.CYAN}{file_path.name}{c.RESET}"
                )

        print(f"\n{Icons.SUCCESS} {c.WHITE}Batch encryption completed!")
        print(
            f"{c.BRIGHT_GREEN}➤{c.WHITE} Successfully encrypted: {c.CYAN}{success_count}/{len(files)}{c.WHITE} files{c.RESET}"
        )

    def batch_backup_all(self, files):
        """Create backup of all files"""
        print(
            f"\n{Icons.INFO} {c.WHITE}Creating backups for {len(files)} files...{c.RESET}"
        )

        success_count = 0
        for file_path in files:
            backup_path = self.file_manager.backup_file(file_path)
            if backup_path:
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Backup created: {c.CYAN}{backup_path.name}{c.RESET}"
                )
                success_count += 1
            else:
                print(
                    f"{Icons.ERROR} {c.WHITE}Failed to backup: {c.CYAN}{file_path.name}{c.RESET}"
                )

        print(f"\n{Icons.SUCCESS} {c.WHITE}Batch backup completed!")
        print(
            f"{c.BRIGHT_GREEN}➤{c.WHITE} Successfully backed up: {c.CYAN}{success_count}/{len(files)}{c.WHITE} files{c.RESET}"
        )

    def generate_file_reports(self, files):
        """Generate detailed file reports"""
        print(
            f"\n{Icons.INFO} {c.WHITE}Generating reports for {len(files)} files...{c.RESET}"
        )

        report_file = f"file_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(report_file, 'w') as f:
            f.write("DuskCipher Pro - File Analysis Report\n")
            f.write("=" * 50 + "\n\n")
            f.write(
                f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(
                f"System: {self.system_info['os']} {self.system_info['platform']}\n"
            )
            f.write(f"User: {self.system_info['username']}\n\n")

            for file_path in files:
                file_info = self.file_manager.get_file_info(file_path)
                f.write(f"File: {file_info['name']}\n")
                f.write(f"Size: {file_info['size']} bytes\n")
                f.write(f"Modified: {file_info['modified']}\n")
                f.write(f"Permissions: {file_info['permissions']}\n")
                f.write(f"Hash: {file_info['hash']}\n")
                f.write("-" * 30 + "\n\n")

        print(
            f"{Icons.SUCCESS} {c.WHITE}Report generated: {c.CYAN}{report_file}{c.RESET}"
        )

    def verify_file_integrity(self, files):
        """Verify file integrity using checksums"""
        print(
            f"\n{Icons.INFO} {c.WHITE}Verifying integrity for {len(files)} files...{c.RESET}"
        )

        integrity_file = 'file_integrity.json'

        if os.path.exists(integrity_file):
            with open(integrity_file, 'r') as f:
                old_hashes = json.load(f)
        else:
            old_hashes = {}

        new_hashes = {}
        changes_detected = False

        for file_path in files:
            file_info = self.file_manager.get_file_info(file_path)
            current_hash = file_info['hash']
            new_hashes[file_path.name] = current_hash

            if file_path.name in old_hashes:
                if old_hashes[file_path.name] != current_hash:
                    print(
                        f"{Icons.WARNING} {c.WHITE}File modified: {c.CYAN}{file_path.name}{c.RESET}"
                    )
                    changes_detected = True
                else:
                    print(
                        f"{Icons.SUCCESS} {c.WHITE}File unchanged: {c.CYAN}{file_path.name}{c.RESET}"
                    )
            else:
                print(
                    f"{Icons.INFO} {c.WHITE}New file detected: {c.CYAN}{file_path.name}{c.RESET}"
                )

        # Save current hashes
        with open(integrity_file, 'w') as f:
            json.dump(new_hashes, f, indent=2)

        if changes_detected:
            print(
                f"\n{Icons.WARNING} {c.WHITE}Some files have been modified since last check!{c.RESET}"
            )
        else:
            print(
                f"\n{Icons.SUCCESS} {c.WHITE}All files integrity verified!{c.RESET}"
            )

    def security_scanner(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_RED}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_RED}║                            🔍 SECURITY SCANNER                                        ║
{c.BRIGHT_RED}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        files = self.file_manager.get_user_files('.sh')

        if not files:
            print(
                f"{Icons.ERROR} {c.WHITE}No .sh files found to scan!{c.RESET}")
            input(
                f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}"
            )
            return

        print(
            f"{Icons.INFO} {c.WHITE}Scanning {len(files)} files for security vulnerabilities...{c.RESET}"
        )

        vulnerabilities = []

        for file_path in files:
            print(
                f"\n{Icons.PROCESS} {c.WHITE}Scanning: {c.CYAN}{file_path.name}{c.RESET}"
            )

            try:
                with open(file_path, 'r') as f:
                    content = f.read()

                # Check for common security issues
                issues = self.check_security_issues(content, file_path.name)
                vulnerabilities.extend(issues)

                if issues:
                    print(
                        f"{Icons.WARNING} {c.WHITE}Found {len(issues)} potential issues{c.RESET}"
                    )
                else:
                    print(f"{Icons.SUCCESS} {c.WHITE}No issues found{c.RESET}")

            except Exception as e:
                print(
                    f"{Icons.ERROR} {c.WHITE}Error scanning {file_path.name}: {str(e)}{c.RESET}"
                )

        # Display results
        print(
            f"\n{c.GOLD}╔═══════════════════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            f"{c.GOLD}║                                SECURITY REPORT                                        ║"
        )
        print(
            f"{c.GOLD}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}"
        )

        if vulnerabilities:
            print(
                f"{Icons.WARNING} {c.WHITE}Found {len(vulnerabilities)} potential security issues:{c.RESET}"
            )
            for i, vuln in enumerate(vulnerabilities, 1):
                print(
                    f"\n{c.BRIGHT_RED}[{i}] {c.WHITE}{vuln['type']}{c.RESET}")
                print(
                    f"    {c.BRIGHT_BLACK}File: {c.CYAN}{vuln['file']}{c.RESET}"
                )
                print(
                    f"    {c.BRIGHT_BLACK}Line: {c.WHITE}{vuln['line']}{c.RESET}"
                )
                print(
                    f"    {c.BRIGHT_BLACK}Description: {c.WHITE}{vuln['description']}{c.RESET}"
                )
        else:
            print(
                f"{Icons.SUCCESS} {c.WHITE}No security issues detected!{c.RESET}"
            )

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def check_security_issues(self, content, filename):
        """Check for common security issues in shell scripts"""
        issues = []
        lines = content.split('\n')

        dangerous_patterns = [
            (r'rm\s+-rf\s+/', 'Dangerous recursive delete'),
            (r'chmod\s+777', 'Insecure file permissions'),
            (r'eval\s+\$', 'Dynamic code execution'),
            (r'curl\s+.*\|\s*bash', 'Piping curl to bash'),
            (r'wget\s+.*\|\s*bash', 'Piping wget to bash'),
            (r'>\s*/dev/null\s+2>&1', 'Suppressing all output'),
            (r'password\s*=\s*["\'].*["\']', 'Hardcoded password'),
            (r'API_KEY\s*=\s*["\'].*["\']', 'Hardcoded API key'),
        ]

        for line_num, line in enumerate(lines, 1):
            for pattern, description in dangerous_patterns:
                import re
                if re.search(pattern, line, re.IGNORECASE):
                    issues.append({
                        'file': filename,
                        'line': line_num,
                        'type': 'Security Warning',
                        'description': description,
                        'content': line.strip()
                    })

        return issues

    def show_statistics(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_GREEN}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_GREEN}║                              📈 USAGE STATISTICS                                      ║
{c.BRIGHT_GREEN}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        stats = self.config['stats']
        files = self.file_manager.get_user_files()

        print(f"{Icons.INFO} {c.WHITE}Application Statistics:{c.RESET}")
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Total Runs: {c.CYAN}{stats['total_runs']}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Files Encrypted: {c.CYAN}{stats['files_encrypted']}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Files Decrypted: {c.CYAN}{stats['files_decrypted']}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Current Files: {c.CYAN}{len(files)}{c.RESET}"
        )

        print(f"\n{Icons.INFO} {c.WHITE}System Information:{c.RESET}")
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}OS: {c.CYAN}{self.system_info['os']}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Platform: {c.CYAN}{self.system_info['platform']}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Python Version: {c.CYAN}{self.system_info['python_version']}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Username: {c.CYAN}{self.system_info['username']}{c.RESET}"
        )

        # Log file statistics
        log_files = list(
            Path('logs').glob('*.log')) if Path('logs').exists() else []
        backup_files = list(
            Path('backups').glob('*')) if Path('backups').exists() else []

        print(f"\n{Icons.INFO} {c.WHITE}File System:{c.RESET}")
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Log Files: {c.CYAN}{len(log_files)}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Backup Files: {c.CYAN}{len(backup_files)}{c.RESET}"
        )

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def system_tools(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_BLUE}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_BLUE}║                             ⚙️  SYSTEM TOOLS                                           ║
{c.BRIGHT_BLUE}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        print(f"{Icons.INFO} {c.WHITE}Available system tools:{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[1] {c.CYAN}System Information{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[2] {c.CYAN}Process Monitor{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[3] {c.CYAN}Network Information{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[4] {c.CYAN}Disk Usage{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[5] {c.CYAN}Environment Variables{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[6] {c.CYAN}Update System{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[0] {c.CYAN}Back to Main Menu{c.RESET}")

        try:
            choice = input(
                f"\n{Icons.QUESTION} {c.WHITE}Select tool: {c.RESET}")

            if choice == '1':
                self.show_system_info()
            elif choice == '2':
                self.show_process_monitor()
            elif choice == '3':
                self.show_network_info()
            elif choice == '4':
                self.show_disk_usage()
            elif choice == '5':
                self.show_environment_variables()
            elif choice == '6':
                self.update_system()
            elif choice == '0':
                return
            else:
                print(f"{Icons.ERROR} {c.WHITE}Invalid choice!{c.RESET}")

        except KeyboardInterrupt:
            print(
                f"\n{Icons.ERROR} {c.WHITE}Operation cancelled by user!{c.RESET}"
            )

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def show_system_info(self):
        """Display detailed system information"""
        print(f"\n{Icons.INFO} {c.WHITE}System Information:{c.RESET}")

        try:
            # Basic system info
            print(
                f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Operating System: {c.CYAN}{self.system_info['os']}{c.RESET}"
            )
            print(
                f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Platform: {c.CYAN}{self.system_info['platform']}{c.RESET}"
            )
            print(
                f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Machine: {c.CYAN}{self.system_info['machine']}{c.RESET}"
            )
            print(
                f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Processor: {c.CYAN}{self.system_info['processor']}{c.RESET}"
            )
            print(
                f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Hostname: {c.CYAN}{self.system_info['hostname']}{c.RESET}"
            )

            # Additional info
            try:
                uptime = subprocess.check_output(['uptime'], text=True).strip()
                print(
                    f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Uptime: {c.CYAN}{uptime}{c.RESET}"
                )
            except:
                pass

            try:
                whoami = subprocess.check_output(['whoami'], text=True).strip()
                print(
                    f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Current User: {c.CYAN}{whoami}{c.RESET}"
                )
            except:
                pass

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Error getting system info: {str(e)}{c.RESET}"
            )

    def show_process_monitor(self):
        """Display running processes"""
        print(f"\n{Icons.INFO} {c.WHITE}Process Monitor:{c.RESET}")

        try:
            result = subprocess.run(['ps', 'aux'],
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                print(
                    f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Total processes: {c.CYAN}{len(lines)-1}{c.RESET}"
                )
                print(f"\n{c.BRIGHT_WHITE}Top 10 processes:{c.RESET}")
                for line in lines[:11]:  # Header + 10 processes
                    print(f"  {c.BRIGHT_BLACK}{line}{c.RESET}")
            else:
                print(
                    f"{Icons.ERROR} {c.WHITE}Could not get process information{c.RESET}"
                )

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Error getting process info: {str(e)}{c.RESET}"
            )

    def show_network_info(self):
        """Display network information"""
        print(f"\n{Icons.INFO} {c.WHITE}Network Information:{c.RESET}")

        try:
            # Get network interfaces
            result = subprocess.run(['ip', 'addr', 'show'],
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                print(
                    f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Network Interfaces:{c.RESET}"
                )
                lines = result.stdout.strip().split('\n')
                for line in lines[:10]:  # Show first 10 lines
                    if line.strip():
                        print(f"    {c.BRIGHT_BLACK}{line}{c.RESET}")

            # Get routing table
            result = subprocess.run(['ip', 'route'],
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                print(
                    f"\n  {c.BRIGHT_GREEN}➤ {c.WHITE}Routing Table:{c.RESET}")
                lines = result.stdout.strip().split('\n')
                for line in lines[:5]:  # Show first 5 routes
                    if line.strip():
                        print(f"    {c.BRIGHT_BLACK}{line}{c.RESET}")

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Error getting network info: {str(e)}{c.RESET}"
            )

    def show_disk_usage(self):
        """Display disk usage information"""
        print(f"\n{Icons.INFO} {c.WHITE}Disk Usage:{c.RESET}")

        try:
            result = subprocess.run(['df', '-h'],
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if line.strip():
                        print(f"  {c.BRIGHT_BLACK}{line}{c.RESET}")

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Error getting disk usage: {str(e)}{c.RESET}"
            )

    def show_environment_variables(self):
        """Display environment variables"""
        print(f"\n{Icons.INFO} {c.WHITE}Environment Variables:{c.RESET}")

        important_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'TERM', 'LANG']

        for var in important_vars:
            value = os.getenv(var, 'Not set')
            print(
                f"  {c.BRIGHT_GREEN}➤ {c.WHITE}{var}: {c.CYAN}{value}{c.RESET}"
            )

    def update_system(self):
        """Update system tools"""
        print(f"\n{Icons.INFO} {c.WHITE}Updating system tools...{c.RESET}")

        try:
            # Update npm packages
            if os.path.exists('package.json'):
                print(
                    f"{Icons.LOADING} {c.WHITE}Updating npm packages...{c.RESET}"
                )
                result = subprocess.run(['npm', 'update'],
                                        capture_output=True,
                                        text=True)
                if result.returncode == 0:
                    print(
                        f"{Icons.SUCCESS} {c.WHITE}npm packages updated successfully{c.RESET}"
                    )
                else:
                    print(
                        f"{Icons.ERROR} {c.WHITE}Failed to update npm packages{c.RESET}"
                    )

            # Update configuration
            print(
                f"{Icons.LOADING} {c.WHITE}Updating configuration...{c.RESET}")
            self.config['updated'] = datetime.now().isoformat()
            if self.config_manager.save_config(self.config):
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Configuration updated successfully{c.RESET}"
                )
            else:
                print(
                    f"{Icons.ERROR} {c.WHITE}Failed to update configuration{c.RESET}"
                )

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Error updating system: {str(e)}{c.RESET}"
            )

    def customization_menu(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_MAGENTA}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_MAGENTA}║                             🎨 CUSTOMIZATION                                          ║
{c.BRIGHT_MAGENTA}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        print(f"{Icons.INFO} {c.WHITE}Customization options:{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[1] {c.CYAN}Change Author Name{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[2] {c.CYAN}Change Community Name{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[3] {c.CYAN}Toggle Auto Backup{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[4] {c.CYAN}Change Log Level{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[5] {c.CYAN}Reset Statistics{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[6] {c.CYAN}Export Configuration{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[0] {c.CYAN}Back to Main Menu{c.RESET}")

        try:
            choice = input(
                f"\n{Icons.QUESTION} {c.WHITE}Select option: {c.RESET}")

            if choice == '1':
                new_author = input(
                    f"{Icons.QUESTION} {c.WHITE}Enter new author name: {c.RESET}"
                )
                self.config['author'] = new_author
                self.config_manager.save_config(self.config)
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Author name updated to: {c.CYAN}{new_author}{c.RESET}"
                )

            elif choice == '2':
                new_community = input(
                    f"{Icons.QUESTION} {c.WHITE}Enter new community name: {c.RESET}"
                )
                self.config['community'] = new_community
                self.config_manager.save_config(self.config)
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Community name updated to: {c.CYAN}{new_community}{c.RESET}"
                )

            elif choice == '3':
                self.config['auto_backup'] = not self.config['auto_backup']
                self.config_manager.save_config(self.config)
                status = "enabled" if self.config['auto_backup'] else "disabled"
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Auto backup {c.CYAN}{status}{c.RESET}"
                )

            elif choice == '4':
                print(
                    f"{Icons.INFO} {c.WHITE}Log levels: debug, info, warning, error{c.RESET}"
                )
                new_level = input(
                    f"{Icons.QUESTION} {c.WHITE}Enter new log level: {c.RESET}"
                )
                if new_level in ['debug', 'info', 'warning', 'error']:
                    self.config['log_level'] = new_level
                    self.config_manager.save_config(self.config)
                    print(
                        f"{Icons.SUCCESS} {c.WHITE}Log level updated to: {c.CYAN}{new_level}{c.RESET}"
                    )
                else:
                    print(
                        f"{Icons.ERROR} {c.WHITE}Invalid log level!{c.RESET}")

            elif choice == '5':
                confirm = input(
                    f"{Icons.WARNING} {c.WHITE}Reset all statistics? (y/N): {c.RESET}"
                )
                if confirm.lower() == 'y':
                    self.config['stats'] = {
                        'files_encrypted': 0,
                        'files_decrypted': 0,
                        'total_runs': 1
                    }
                    self.config_manager.save_config(self.config)
                    print(
                        f"{Icons.SUCCESS} {c.WHITE}Statistics reset successfully{c.RESET}"
                    )
                else:
                    print(
                        f"{Icons.INFO} {c.WHITE}Statistics reset cancelled{c.RESET}"
                    )

            elif choice == '6':
                export_file = f"duskcipher_config_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(export_file, 'w') as f:
                    json.dump(self.config, f, indent=2)
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Configuration exported to: {c.CYAN}{export_file}{c.RESET}"
                )

            elif choice == '0':
                return
            else:
                print(f"{Icons.ERROR} {c.WHITE}Invalid choice!{c.RESET}")

        except KeyboardInterrupt:
            print(
                f"\n{Icons.ERROR} {c.WHITE}Operation cancelled by user!{c.RESET}"
            )

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def backup_manager(self):
        self.clear_screen()
        print(f"""
{c.BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════════════════╗
{c.BRIGHT_CYAN}║                             💾 BACKUP MANAGER                                         ║
{c.BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════════════════╝{c.RESET}
""")

        backup_files = list(
            Path('backups').glob('*')) if Path('backups').exists() else []

        print(
            f"{Icons.INFO} {c.WHITE}Available backups: {c.CYAN}{len(backup_files)}{c.RESET}"
        )

        if backup_files:
            print(f"\n{Icons.FOLDER} {c.WHITE}Backup files:{c.RESET}")
            for i, backup_file in enumerate(backup_files[:10],
                                            1):  # Show first 10
                file_info = self.file_manager.get_file_info(backup_file)
                print(
                    f"  {c.BRIGHT_WHITE}[{i:2d}] {c.CYAN}{backup_file.name:<30}{c.WHITE} ({file_info['size']} bytes) {c.BRIGHT_BLACK}{file_info['modified']}{c.RESET}"
                )

        print(f"\n{Icons.INFO} {c.WHITE}Backup operations:{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[1] {c.CYAN}Create Full Backup{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[2] {c.CYAN}Restore from Backup{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[3] {c.CYAN}Clean Old Backups{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[4] {c.CYAN}Backup Statistics{c.RESET}")
        print(f"  {c.BRIGHT_WHITE}[0] {c.CYAN}Back to Main Menu{c.RESET}")

        try:
            choice = input(
                f"\n{Icons.QUESTION} {c.WHITE}Select operation: {c.RESET}")

            if choice == '1':
                self.create_full_backup()
            elif choice == '2':
                self.restore_from_backup(backup_files)
            elif choice == '3':
                self.clean_old_backups(backup_files)
            elif choice == '4':
                self.backup_statistics(backup_files)
            elif choice == '0':
                return
            else:
                print(f"{Icons.ERROR} {c.WHITE}Invalid choice!{c.RESET}")

        except KeyboardInterrupt:
            print(
                f"\n{Icons.ERROR} {c.WHITE}Operation cancelled by user!{c.RESET}"
            )

        input(
            f"\n{Icons.QUESTION} {c.WHITE}Press Enter to continue...{c.RESET}")

    def create_full_backup(self):
        """Create a full backup of all user files"""
        files = self.file_manager.get_user_files()

        if not files:
            print(f"{Icons.ERROR} {c.WHITE}No files to backup!{c.RESET}")
            return

        print(
            f"\n{Icons.INFO} {c.WHITE}Creating full backup of {len(files)} files...{c.RESET}"
        )

        success_count = 0
        for file_path in files:
            backup_path = self.file_manager.backup_file(file_path)
            if backup_path:
                print(
                    f"{Icons.SUCCESS} {c.WHITE}Backed up: {c.CYAN}{file_path.name}{c.RESET}"
                )
                success_count += 1
            else:
                print(
                    f"{Icons.ERROR} {c.WHITE}Failed to backup: {c.CYAN}{file_path.name}{c.RESET}"
                )

        print(f"\n{Icons.SUCCESS} {c.WHITE}Full backup completed!")
        print(
            f"{c.BRIGHT_GREEN}➤{c.WHITE} Successfully backed up: {c.CYAN}{success_count}/{len(files)}{c.WHITE} files{c.RESET}"
        )

    def restore_from_backup(self, backup_files):
        """Restore files from backup"""
        if not backup_files:
            print(
                f"{Icons.ERROR} {c.WHITE}No backup files available!{c.RESET}")
            return

        print(
            f"\n{Icons.INFO} {c.WHITE}Available backups for restoration:{c.RESET}"
        )
        for i, backup_file in enumerate(backup_files[:10], 1):
            print(
                f"  {c.BRIGHT_WHITE}[{i}] {c.CYAN}{backup_file.name}{c.RESET}")

        try:
            choice = input(
                f"{Icons.QUESTION} {c.WHITE}Select backup to restore (number): {c.RESET}"
            )

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(backup_files):
                    backup_file = backup_files[index]

                    # Extract original filename
                    original_name = '_'.join(
                        backup_file.stem.split('_')[:-2]) + backup_file.suffix

                    confirm = input(
                        f"{Icons.WARNING} {c.WHITE}Restore {backup_file.name} as {original_name}? (y/N): {c.RESET}"
                    )
                    if confirm.lower() == 'y':
                        try:
                            with open(backup_file,
                                      'rb') as src, open(original_name,
                                                         'wb') as dst:
                                dst.write(src.read())
                            print(
                                f"{Icons.SUCCESS} {c.WHITE}File restored successfully: {c.CYAN}{original_name}{c.RESET}"
                            )
                        except Exception as e:
                            print(
                                f"{Icons.ERROR} {c.WHITE}Restore failed: {str(e)}{c.RESET}"
                            )
                    else:
                        print(
                            f"{Icons.INFO} {c.WHITE}Restore cancelled{c.RESET}"
                        )
                else:
                    print(
                        f"{Icons.ERROR} {c.WHITE}Invalid backup number!{c.RESET}"
                    )
            else:
                print(
                    f"{Icons.ERROR} {c.WHITE}Please enter a valid number!{c.RESET}"
                )

        except Exception as e:
            print(
                f"{Icons.ERROR} {c.WHITE}Error during restore: {str(e)}{c.RESET}"
            )

    def clean_old_backups(self, backup_files):
        """Clean old backup files"""
        if not backup_files:
            print(f"{Icons.ERROR} {c.WHITE}No backup files to clean!{c.RESET}")
            return

        # Sort by modification time (oldest first)
        backup_files.sort(key=lambda x: x.stat().st_mtime)

        if len(backup_files) <= 5:
            print(
                f"{Icons.INFO} {c.WHITE}Less than 5 backups found, no cleaning needed{c.RESET}"
            )
            return

        old_backups = backup_files[:-5]  # Keep only last 5

        print(
            f"\n{Icons.INFO} {c.WHITE}Found {len(old_backups)} old backups to clean:{c.RESET}"
        )
        for backup in old_backups:
            print(f"  {c.BRIGHT_BLACK}• {backup.name}{c.RESET}")

        confirm = input(
            f"\n{Icons.WARNING} {c.WHITE}Delete {len(old_backups)} old backups? (y/N): {c.RESET}"
        )
        if confirm.lower() == 'y':
            deleted_count = 0
            for backup in old_backups:
                try:
                    backup.unlink()
                    print(
                        f"{Icons.SUCCESS} {c.WHITE}Deleted: {c.CYAN}{backup.name}{c.RESET}"
                    )
                    deleted_count += 1
                except Exception as e:
                    print(
                        f"{Icons.ERROR} {c.WHITE}Failed to delete {backup.name}: {str(e)}{c.RESET}"
                    )

            print(
                f"\n{Icons.SUCCESS} {c.WHITE}Cleanup completed! Deleted {deleted_count} old backups{c.RESET}"
            )
        else:
            print(f"{Icons.INFO} {c.WHITE}Cleanup cancelled{c.RESET}")

    def backup_statistics(self, backup_files):
        """Show backup statistics"""
        if not backup_files:
            print(
                f"{Icons.ERROR} {c.WHITE}No backup files available!{c.RESET}")
            return

        print(f"\n{Icons.INFO} {c.WHITE}Backup Statistics:{c.RESET}")

        total_size = sum(f.stat().st_size for f in backup_files)
        oldest_backup = min(backup_files, key=lambda x: x.stat().st_mtime)
        newest_backup = max(backup_files, key=lambda x: x.stat().st_mtime)

        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Total Backups: {c.CYAN}{len(backup_files)}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Total Size: {c.CYAN}{total_size} bytes ({total_size/1024:.2f} KB){c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Oldest Backup: {c.CYAN}{oldest_backup.name}{c.RESET}"
        )
        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}Newest Backup: {c.CYAN}{newest_backup.name}{c.RESET}"
        )

        # File type distribution
        file_types = {}
        for backup in backup_files:
            ext = backup.suffix.lower()
            file_types[ext] = file_types.get(ext, 0) + 1

        print(
            f"  {c.BRIGHT_GREEN}➤ {c.WHITE}File Types: {c.CYAN}{', '.join([f'{ext}({count})' for ext, count in file_types.items()])}{c.RESET}"
        )

    def run(self):
        """Main application loop"""
        try:
            while True:
                self.clear_screen()
                self.display_banner()
                self.display_main_menu()

                choice = input(
                    f"\n{c.WHITE}┌─[{c.CYAN}{self.config['author']}{c.WHITE}@{c.CYAN}{self.config['community']}{c.WHITE}]\n└─{c.BRIGHT_GREEN}$ {c.RESET}"
                )

                if choice == "1" or choice.lower() == "encrypt":
                    self.encrypt_script()
                elif choice == "2" or choice.lower() == "decrypt":
                    self.decrypt_script()
                elif choice == "3" or choice.lower() == "analyze":
                    self.file_analyzer()
                elif choice == "4" or choice.lower() == "batch":
                    self.batch_operations()
                elif choice == "5" or choice.lower() == "security":
                    self.security_scanner()
                elif choice == "6" or choice.lower() == "stats":
                    self.show_statistics()
                elif choice == "7" or choice.lower() == "system":
                    self.system_tools()
                elif choice == "8" or choice.lower() == "custom":
                    self.customization_menu()
                elif choice == "9" or choice.lower() == "backup":
                    self.backup_manager()
                elif choice == "0" or choice.lower() in ["exit", "quit"]:
                    self.clear_screen()
                    print(f"""

                             THANK YOU FOR USING                                     
                            DUSKCIPHER PRO TOOLKIT                                    
                                                                                       
                    Created with {c.BRIGHT_RED}❤️{c.BRIGHT_GREEN} by {c.CYAN}{self.config['author']}{c.BRIGHT_GREEN} & {c.CYAN}{self.config['community']}{c.BRIGHT_GREEN}                       
""")
                    Animations.typewriter(
                        f"{c.CYAN}🌟 Stay secure, stay protected! 🌟{c.RESET}")
                    print(f"\n{c.BRIGHT_WHITE}👋 See you next time!{c.RESET}\n")
                    break
                else:
                    print(
                        f"{Icons.ERROR} {c.WHITE}Invalid choice! Please select 0-9 or use command names.{c.RESET}"
                    )
                    time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n\n{Icons.SUCCESS} {c.CYAN}Goodbye! 👋{c.RESET}")
        except Exception as e:
            print(
                f"\n{Icons.ERROR} {c.WHITE}An unexpected error occurred: {str(e)}{c.RESET}"
            )
            self.logger.log('error', f'Unexpected error: {str(e)}')


if __name__ == "__main__":
    app = DuskCipherPro()
    app.run()
