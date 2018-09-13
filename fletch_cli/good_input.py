# for better, authenticated, well formated input with error handling.

def get_input(prompt="Type something", expected_type="String"):

    prompt += '\n>>> '
    answer = ''

    try:
        while True:
            answer = str(input(prompt))

            if expected_type.lower() in ['enter', 'return']:
                break

            elif answer == '':
                print("You didn't type anything.")

            elif expected_type.lower() in ['str', 'string']:
                break

            elif expected_type.lower() in ['int', 'integer']:
                try:
                    answer = int(answer)
                    break
                except:
                    print("that wasn't an Integer.")

            elif expected_type.lower() in ['val', 'value', 'float']:
                try:
                    answer = float(answer)
                    break
                except:
                    print("that wasn't a Float.")

            elif expected_type.lower() in ['bool', 'boolean', 'tf', 'yn']:
                answer = str(answer)
                if answer.lower() in ['y', 'yes', 'true', 't', '1']:
                    answer = True
                    break

                elif answer.lower() in ['n', 'no', 'false', 'f', '0']:
                    answer = False
                    break

                else:
                    print("Couldn't use that as a boolean.")

            else:
                print("Try Again.")

        return answer

    except KeyboardInterrupt:
        print()
        exit()

if __name__ == "__main__":
    print(get_input('Type stuff to test', 'bool'))
    input('press enter ')
