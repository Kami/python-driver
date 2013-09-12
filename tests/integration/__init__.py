import os

if not os.getenv('TRAVIS', None):
    # Only TravisCI we don't use ccm to start a cassandra cluster and we simply
    # depend on the Cassandra provided by TravisCI.
    from tests.integration.ccm import setup_package, teardown_package
