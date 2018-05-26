import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print ('________________________')
    print ('      Journal App ')
    print('________________________')

def run_event_loop():
    print('What do you want to do with the journal?')

    journal_name = 'default'
    journal_data = journal.load(journal_name)

    cmd = None
    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'x':
            print ('Good bye')
        else:
            print ("Sorry, we don't understand '{}'. " .format(cmd))
        journal.save(journal_name, journal_data)

def list_entries(data):
    entries = reversed(data)
    for (idx, entry) in enumerate(entries):
        print ('* [{}] {}' .format(idx+1, entry))

def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text)


main()