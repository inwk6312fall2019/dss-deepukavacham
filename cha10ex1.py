def sum_nested(List):
        new_List = []
        def flatlist(List):
                for i in range(len(List)):
                        if type(List[i]) == int:
                                new_List.append(List[i])
                        else:
                                flatlist(nestedList[i])
                return new_List
		flatlist(List)
        print sum(new_List)
sum_nested(List)
