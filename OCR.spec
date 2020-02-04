# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src\\ocr\\OCR.py'],
             pathex=['D:\\OneDrive\\Research\\robot-personal-1'],
             binaries=[],
             datas=[('C:/Users/zjplab/Miniconda3/envs/wechat/Lib/site-packages/mxnet*', './mxnet'), ('C:/Users/zjplab/Miniconda3/envs/wechat/Lib/site-packages/snownlp', './snownlp')],
             hiddenimports=['PyQt5.sip', 'pandas', 'pandas._libs.tslibs.timedeltas', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.skiplist'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='OCR',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
