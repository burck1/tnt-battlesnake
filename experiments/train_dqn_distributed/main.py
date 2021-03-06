import argparse
import os
from types import SimpleNamespace

from sacred import Experiment

from experiments.train_dqn_distributed.main_actor import main_actor
from experiments.train_dqn_distributed.main_learner import main_learner

ex = Experiment("train_dqn_distributed")
base_config_path = os.path.dirname(__file__) + "/../dqn_base_config.json"
ex.add_config(base_config_path)
config_path = os.path.dirname(__file__) + "/config.json"
ex.add_config(config_path)

@ex.automain
def main(_run, _config):
    parser = argparse.ArgumentParser()
    parser.add_argument("--actor", type=int)
    parser.add_argument("--learner_address", type=str)
    args, _ = parser.parse_known_args()

    config = SimpleNamespace(**_config)
    run_id = _run._id

    if args.learner_address:
        config.distributed["learner_address"] = args.learner_address

    if args.actor:
        main_actor(run_id, config, args.actor)
    else:
        main_learner(run_id, config)
