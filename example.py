# vim: fileencoding=utf-8

import argparse
import configparser
import logging.config

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", default="src_dir", help="source directory (src_dir)")
    parser.add_argument("dst", default="dst_dir", help="destination directory (dst_dir)")
    parser.add_argument("--foo", default="test", help="optional string foo (test)")
    parser.add_argument("--optional-num", default=5, type=int, help="intのみを受け付けるオプション (5)")
    parser.add_argument("--sw1", action="store_true", help="switch 1, オプションを付けるとsw2はtrue (false)")
    parser.add_argument("--sw2", action="store_false", help="switch 2, オプションを付けるとsw2はfalse (true)")
    args = parser.parse_args()

    # ログ設定ファイルからログ設定を読み込み
    logging.config.fileConfig("log.ini")
    logger = logging.getLogger()

    logger.log(20, "info")
    logger.log(30, "warning")
    logger.log(100, "test")

    logger.info("info")
    logger.warning("warning")

    logger.debug("args")
    logger.debug("src = %s" % args.src)
    logger.debug("dst = %s" % args.dst)
    logger.debug("foo = %s" % args.dst)
    logger.debug("optional-num(optional_num) = %s" % args.optional_num)
    logger.debug("sw1 = %s" % args.sw1)
    logger.debug("sw2 = %s" % args.sw2)

    conf = configparser.ConfigParser()
    conf.read("conf.ini", "UTF-8")

    if conf.get("settings", "bool_test") == "True":
        logger.info(conf.get("settings", "nihongo"))


if __name__ == "__main__":
    main()
