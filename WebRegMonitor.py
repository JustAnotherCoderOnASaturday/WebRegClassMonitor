from Course import courseTitle


def main():
    department = input('Enter Course Department: ')
    courseID = input('Enter Course ID: ')

    siteDetails = courseTitle(department, courseID)

    while True:
        if siteDetails.checkCourseAvailability():
            print('!!!!! COURSE IS AVAILIBLE !!!!!')
            break

        print('[*] No Changes Have Been Made')
        siteDetails.pauseTime()


if __name__ == '__main__':
    main()

    print('[+] Scraper Is Completed')