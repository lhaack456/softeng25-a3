import pytest

from pmgr.project import Project
from pmgr.project import TaskException

@pytest.fixture(scope="function")
def testproj():
    tproj = Project('mytestproj')
    yield tproj
    tproj.delete()

def test_add(testproj):
    testproj.add_task('dosomething')
    assert 'dosomething' in testproj.get_tasks()

def test_del_task(testproj):
    testproj.add_task('task1')
    testproj.remove_task('task1')
    assert 'task1' not in testproj.get_tasks()

def test_several_tasks(testproj):
    tasks = ['task1','task2','task3']
    for t in tasks:
        testproj.add_task(t)
    assert (testproj.get_tasks()) == (tasks)

def test_fail_remove_task(testproj):
    tasks = []
    with pytest.raises(TaskException):
        testproj.remove_task('task1')
    
def test_add_exists_already(testproj):
    testproj.add_task('somethinghere')
    with pytest.raises(TaskException):
        assert 'somethinghere' in testproj.get_tasksdef test_add_exists_already(testproj):
    testproj.add_task('somethinghere')
    with pytest.raises(TaskException) as x:
        testproj.add_task('somethinghere')
    assert 'already exists' in str(x.value)
