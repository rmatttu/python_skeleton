# vim: fileencoding=utf-8

import configparser
import logging.config

def main():
    # ログ設定ファイルからログ設定を読み込み
    logging.config.fileConfig('log.ini')

    logger = logging.getLogger()

    logger.log(20, 'info')
    logger.log(30, 'warning')
    logger.log(100, 'test')

    logger.info('info')
    logger.warning('warning')

    conf = configparser.ConfigParser()
    conf.read('conf.ini', 'UTF-8')

    if conf.get('settings', 'bool_test') == "True":
        logger.info(conf.get('settings', 'nihongo'))


if __name__ == '__main__':
    main()
