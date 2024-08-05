import sys
import os
import yaml
import json
from argparse import Namespace
import run

from run import summary_logs, analysis_log, get_valid_cases

from utils import flagperf_logger
RUN_LOGGER = flagperf_logger.FlagPerfLogger()
run.RUN_LOGGER = RUN_LOGGER

def main(curr_log_path):
    with open("configs/host.yaml", "r") as file:
        config_dict = yaml.safe_load(file)
        config = Namespace(**config_dict)
    RUN_LOGGER.init(curr_log_path,
                    "tmp_analysis_log.log",
                    config.FLAGPERF_LOG_LEVEL,
                    "both",
                    log_caller=True)
    cases = get_valid_cases(config)
    for case in cases:
        RUN_LOGGER.info("======= Testcase: " + case + " =======")
        RUN_LOGGER.info("1) summary logs")
        case_log_dir = os.path.join(curr_log_path, case)
        key_logs = summary_logs(config, case_log_dir)
        RUN_LOGGER.debug(key_logs)
        jsonfile = os.path.join(curr_log_path, "tmp_detail_result.json")
        json.dump(key_logs, open(jsonfile, "w"))

        RUN_LOGGER.info("2) analysis logs")
        analysis_log(key_logs)







if __name__ == "__main__":
    main(sys.argv[1])