from Course import courseTitle


def main():
    department = input('Enter Course Department: ')
    courseID = input('Enter Course ID: ')
    waitTime = input('Wait Time(s) [Default is 360]: ')
    waitTime = int(waitTime) if waitTime != "" else 360

    siteDetails = courseTitle(department, courseID, waitTime)

    while True:
        if siteDetails.checkCourseAvailability():
            print('!!!!! COURSE IS AVAILIBLE !!!!!')
            break

        print('[*] No Changes Have Been Made')
        siteDetails.pauseTime()


if __name__ == '__main__':
    main()

    print('[+] Scraper Is Completed')