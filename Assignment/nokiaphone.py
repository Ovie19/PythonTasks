exit = False
menu_type = "A"

phone_book_menu = """1. Search\n2. Service Nos\n3. Add name\n4. Erase\n5. Edit
6. Assign tone\n7. Send b'card\n8. Options\n9. Speed dials\n10. Voice tags"""

messages_menu = """1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages
5. Templates\n6. Smileys\n7. Message settings\n8. Info service
9. Voice mailbox number\n10. Service command editor"""

call_register_menu = """1. Missed calls\n2. Received callss\n3. Dialled numbers
4. Erase recent call lists\n5. Show call duration\n6. Show call costs
7. Call cost settings\n8. Prepaid credit"""

tones_menu = """1. Ringing tone\n2. Ringing volume\n3. Incoming call alert
4. Composer\n5. Message alert tone\n6. Keypad tones\n7. Warning and game tones
8. Vibrating alert\n9. Screen saver"""

settings_menu = "1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory settings"

clock_menu = """1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch
5. Countdown timer\n6. Auto update of date and time"""

while not exit:
    if menu_type == "A":
        print("\nNokia 3310 Menu", "1. Phone book", "2. Messages", "3. Chat", sep="\n")
        print("4. Call register", "5. Tones", "6. Settings", "7. Call divert", sep="\n")
        print("8. Games", "9. Calculator", "10. Reminder", "11. Clock", sep="\n")
        print("12. Profiles", "13. SIM services", "0. Exit", sep="\n")
        menu_choice = input("Enter choice: ")
        if menu_choice == "0":
            exit = True
        else:
            menu_type = "B"

    if menu_type == "B":
        match menu_choice:
            case "1":
                print("\nPhone book")
                print(phone_book_menu)
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
                else:
                    menu_type = "C"
            case "2":
                print("\nMessages")
                print(messages_menu)
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
                else:
                    menu_type = "C"
            case "3":
                print("\nChat")
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
            case "4":
                print("\nCall register")
                print(call_register_menu)
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
                else:
                    menu_type = "C"
            case "5":
                print("\nTones")
                print(tones_menu)
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
                else:
                    menu_type = "C"
            case "6":
                print("\nSettings")
                print(settings_menu)
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
                else:
                    menu_type = "C"
            case "7":
                print("\nCall divert")
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
            case "8":
                print("\nGames")
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
            case "9":
                print("\nCalculator")
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
            case "10":
                print("\nReminder")
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
            case "11":
                print("\nClock")
                print(clock_menu)
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
                else:
                    menu_type = "C"
            case "12":
                print("\nProfiles")
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"
            case "13":
                print("\nSIM services")
                print("0. Return to menu")
                sub_menu_choice = input("Enter choice: ")
                if sub_menu_choice == "0":
                    menu_type = "A"

    if menu_type == "C":
        # PHONE BOOKS
        if menu_choice == "1":
            match sub_menu_choice:
                case "1":
                    print("\nSearch")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "2":
                    print("\nService Nos.")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "3":
                    print("\nAdd name")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "4":
                    print("\nErase")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "5":
                    print("\nEdit")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "6":
                    print("\nAssign tone")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "7":
                    print("\nSend b'card")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "8":
                    print("\nOptions")
                    print("1. Type of view\n2. Memory status")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == "1":
                            print("\nType of view")
                        if sub_sub_menu_choice == "2":
                            print("\nMemory status")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "9":
                    print("\nSpeed dials")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "10":
                    print("\nVoice tags")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"

        # MESSAGES
        if menu_choice == "2":
            match sub_menu_choice:
                case "1":
                    print("\nWrite messages")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "2":
                    print("\nInbox")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "3":
                    print("\nOutbox")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "4":
                    print("\nPicture messages")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "5":
                    print("\nTemplates")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "6":
                    print("\nSmileys")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "7":
                    print("\nMessages settings")
                    print("1. Set 1\n2. Common")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == "1":
                            print("\nSet 1")
                        if sub_sub_menu_choice == "2":
                            print("\nCommon")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "8":
                    print("\nInfo service")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "9":
                    print("\nVoice mailbox number")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "10":
                    print("\nService command editor")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"

        # CALL REGISTERS
        if menu_choice == "4":
            match sub_menu_choice:
                case "1":
                    print("\nMissed calls")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "2":
                    print("\nReceived calls")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "3":
                    print("\nDialled numbers")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "4":
                    print("\nErase recent call lists")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "5":
                    print("\nShow call duration")
                    print("1. Last call duration\n2. All calls' duration\n3. Received calls' duration")
                    print("4. Dialled calls' duration\n5. Clear timers\n0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == "1":
                            print("\nLast call duration")
                        if sub_sub_menu_choice == "2":
                            print("\nAll calls' duration")
                        if sub_sub_menu_choice == "3":
                            print("\nReceived calls' duration")
                        if sub_sub_menu_choice == "4":
                            print("\nDialled calls' duration")
                        if sub_sub_menu_choice == "5":
                            print("\nClear timers")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "6":
                    print("\nShow call costs")
                    print("1. Last call cost\n2. All calls' costs\n3. Clear counters")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == "1":
                            print("\nLast call cost")
                        if sub_sub_menu_choice == "2":
                            print("\nAll calls' costs")
                        if sub_sub_menu_choice == "3":
                            print("\nClear counters")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "7":
                    print("\nCall cost settings")
                    print("1. Call cost limit\n2. Show costs in")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == "1":
                            print("\nCall cost limit")
                        if sub_sub_menu_choice == "2":
                            print("\nShow costs in")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "8":
                    print("\nPrepaid")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"

        # TONES
        if menu_choice == "5":
            match sub_menu_choice:
                case "1":
                    print("\nRinging tone")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "2":
                    print("\nRinging volume")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "3":
                    print("\nIncoming call alert")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "4":
                    print("\nComposer")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "5":
                    print("\nMessage alert tone")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "6":
                    print("\nKeypad tones")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "7":
                    print("\nWarning and game tones")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "8":
                    print("\nVibrating alert")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "9":
                    print("\nScreen saver")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"

        # SETTINGS
        if menu_choice == "6":
            match sub_menu_choice:
                case "1":
                    print("\nCall settings")
                    print("1. Automatic redial\n2. Speed dialling\n3. Call waiting options")
                    print("4. Own number sending\n5. Phone line in use\n6. Automatic answer")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == "1":
                            print("\nAutomatic redial")
                        if sub_sub_menu_choice == "2":
                            print("\nSpeed dialling")
                        if sub_sub_menu_choice == "3":
                            print("\nCall waiting options")
                        if sub_sub_menu_choice == "4":
                            print("\nOwn number sending")
                        if sub_sub_menu_choice == "5":
                            print("\nPhone line in use")
                        if sub_sub_menu_choice == "6":
                            print("\nAutomatic answer")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "2":
                    print("\nPhone settings")
                    print("1. Language\n2. Cell info display\n3. Welcome note")
                    print("4. Network selection\n5. Lights\n6. Confirm SIM service actions")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == "1":
                            print("\nLanguage")
                        if sub_sub_menu_choice == "2":
                            print("\nCell info display")
                        if sub_sub_menu_choice == "3":
                            print("\nWelcome note")
                        if sub_sub_menu_choice == "4":
                            print("\nNetwork selection")
                        if sub_sub_menu_choice == "5":
                            print("\nLights")
                        if sub_sub_menu_choice == "6":
                            print("\nConfirm SIM service actions")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "3":
                    print("\nSecurity settings")
                    print("1. PIN code request\n2. Call barring service\n3. Fixed dialling")
                    print("4. Closed user group\n5. Phone security\n6. Change access codes")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                    else:
                        if sub_sub_menu_choice == 1:
                            print("\nPIN code request")
                        if sub_sub_menu_choice == 2:
                            print("\nCall barring service")
                        if sub_sub_menu_choice == 3:
                            print("\nFixed dialling")
                        if sub_sub_menu_choice == 4:
                            print("\nClosed user group")
                        if sub_sub_menu_choice == 5:
                            print("\nPhone security")
                        if sub_sub_menu_choice == 6:
                            print("\nChange access codes")

                        sub_sub_menu_choice = input("Enter 0 to go back: ")
                case "4":
                    print("\nComposer")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"

        # CLOCK
        if menu_choice == "11":
            match sub_menu_choice:
                case "1":
                    print("\nAlarm clock")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "2":
                    print("\nClock settings")
                    print("0. Return to menu")
                    print("Enter choice: ")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "3":
                    print("\nDate setting")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "4":
                    print("\nStopwatch")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "5":
                    print("\nCountdown timer")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
                case "6":
                    print("\nAuto update of date and time")
                    print("0. Return to menu")
                    sub_sub_menu_choice = input("Enter choice: ")
                    if sub_sub_menu_choice == "0":
                        menu_type = "B"
