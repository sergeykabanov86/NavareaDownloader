from navarea.navarea_parser import navarea_parser
from navarea import navarea_class
from sealagom.data import collect_data, collect_data_tmp



def main():
    for i in range(1,20):
        if(i == 13):
            continue
        navareas = collect_data_tmp(i)

        print('Парсим наварию {i}!')
        print(navareas)

        #Здесь надо разбить наварию на сообщения


        navarea = navarea_parser()













if __name__ == '__main__':
    main()