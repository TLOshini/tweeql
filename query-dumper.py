from ssql.exceptions import SSQLException
from ssql.builtin_functions import register
from ssql.query_runner import DbInsertStatusHandler
from ssql.query_runner import QueryRunner
from time import sleep

import settings
import traceback

def main():
    register()
    insert_handler = DbInsertStatusHandler('tester2', 'sqlite:///test.db')
    runner = QueryRunner(insert_handler, batch_size=10)
    try:
        while True:
            cmd = raw_input("ssql> ");
            process_command(runner, cmd)
    except KeyboardInterrupt:
        print '\nGoodbye!'

def process_command(runner, cmd):
    try:
        runner.run_query(cmd, False)
    except KeyboardInterrupt:
        runner.stop_query()
    except SSQLException, e:
        runner.stop_query()
        if settings.DEBUG:
            traceback.print_exc()
        else:
            print e

if __name__ == '__main__':
    main()
