def priority_sort(array, priorities):
    def custom_sort(elem):
        return (elem in priorities, elem)


    array.sort(key=custom_sort)
    print(array)

    return array




def main():
    priority_sort([6,2,9,1,5], [1,2,9])
        
if __name__ == '__main__':
    main()
