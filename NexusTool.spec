# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Collect data files from pyfiglet
pyfiglet_fonts = collect_data_files('pyfiglet', subdir='fonts')

a = Analysis(
    ['NexusTool.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('ifcon.ico', '.'),  # Correct path for the new icon file
        *pyfiglet_fonts
    ],
    hiddenimports=['pyfiglet'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='NexusTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to True for console mode, False for GUI mode
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='ifcon.ico',  # Ensure the correct icon file is referenced
)
