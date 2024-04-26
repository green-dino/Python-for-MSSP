import datetime
import pprint
from systemd import journal
import select

def read_journal_entries():
    # Create a systemd.journal.Reader instance
    j = journal.Reader()

    # Set the reader's default log level
    j.log_level(journal.LOG_INFO)

    # Only include entries since the current box has booted.
    j.this_boot()
    j.this_machine()

    # Filter log entries
    j.add_match(
        _SYSTEMD_UNIT=u'myservice.service',
        SYSLOG_IDENTIFIER=u'myservice/module',
        _COMM=u'myservicecommand'
    )

    # Move to the end of the journal
    j.seek_tail()

    # Important! - Discard old journal entries
    j.get_previous()

    # Create a poll object for journal entries
    p = select.poll()

    # Register the journal's file descriptor with the polling object.
    journal_fd = j.fileno()
    poll_event_mask = j.get_events()
    p.register(journal_fd, poll_event_mask)

    # Poll for new journal entries every 250ms
    while True:
        if p.poll(250):
            if j.process() == journal.APPEND:
                for entry in j:
                    pprint.pprint(entry)

        print('waiting ... %s' % datetime.datetime.now())

if __name__ == "__main__":
    read_journal_entries()
