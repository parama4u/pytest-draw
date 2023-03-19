from random import Random
def pytest_addoption(parser):
    group = parser.getgroup("sanity", "sanity tests to run")
    group.addoption('--sanity',
                    action="store_true",
                    dest="sanity",
                    default=False,
                    help="Consider or ignore the execution as Sanity test. Defaults to False, "
                    )

    group.addoption('--max_test',
                    action="store",
                    dest="max_test",
                    default=5,
                    help="Maximum tests to run. Defaults to 5"
                    )


def pytest_report_header(config):
    if config.option.sanity:
        return f"Configured for Sanity. Max tests would be:{config.option.max_test}"


def pytest_collection_modifyitems(session, config, items):
    """ called after collection has been performed, may filter or re-order
    the items in-place."""
    if not config.option.sanity:
        return
    random = Random()
    random.shuffle(items)
    session.items = random.sample(items, int(config.option.max_test))
