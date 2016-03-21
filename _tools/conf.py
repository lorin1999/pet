from plumbum import LocalPath

PROJECT_PATH = LocalPath(__file__).dirname.up()
""":type: LocalPath"""

OUTPUT_PATH = PROJECT_PATH / '_output'
""":type: LocalPath"""
