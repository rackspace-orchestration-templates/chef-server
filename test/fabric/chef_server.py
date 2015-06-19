from fabric.api import env, task
from envassert import detect, file, group, package, port, process, service, \
    user
from hot.utils.test import get_artifacts


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("chef-server-core")
    assert file.exists("/etc/opscode/chef-server.rb")
    assert port.is_listening(80)
    assert port.is_listening(443)
    assert user.exists("opscode")
    assert group.is_exists("opscode")
    assert user.is_belonging_group("opscode", "opscode")
    assert process.is_up("nginx")
    assert process.is_up("postgres")
    assert service.is_enabled("nginx")
    assert service.is_enabled("postgres")


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
