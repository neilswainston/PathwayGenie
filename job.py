'''
PathwayGenie (c) University of Manchester 2015

PathwayGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
from threading import Thread


class JobThread(Thread):
    '''Wraps a job into a thread, and fires events.'''

    def __init__(self, job_id):
        Thread.__init__(self)
        self.__job_id = job_id
        self.__listeners = set()

    def add_listener(self, listener):
        '''Adds an event listener.'''
        self.__listeners.add(listener)

    def remove_listener(self, listener):
        '''Removes an event listener.'''
        self.__listeners.remove(listener)

    def run(self):
        self.__do_job()

    def __do_job(self):
        '''Performs the task. Should be overridden.'''
        import time

        progress = 0

        while progress < 100:
            time.sleep(0.1)
            evt = {'job_id': self.__job_id, 'progress': progress}
            self._fire_event(evt)
            progress += 1

        evt = {'job_id': self.__job_id, 'progress': progress}
        self._fire_event(evt)

    def _fire_event(self, event):
        '''Fires an event to event listeners.'''
        for listener in self.__listeners:
            listener.event_fired(event)
