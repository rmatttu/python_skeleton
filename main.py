# vim: fileencoding=utf-8

import logging.config

def main():
    # ログ設定ファイルからログ設定を読み込み
    logging.config.fileConfig('system/logging.conf')

    logger = logging.getLogger()

    logger.log(20, 'info')
    logger.log(30, 'warning')
    logger.log(100, 'test')

    logger.info('info')
    logger.warning('warning')

if __name__ == '__main__':
    main()
