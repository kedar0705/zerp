def find_category_best_guesses(category):
    """
    This method is used to find the best category guesses from the categories we got from the different systems
    :param category: the category model which holds the values of the different systems
    :return: list of ranked categories
    """
    public_data, label_data, llm_data = 'public_data', 'label_data', 'llm_data'
    base_key_order = [public_data, label_data, llm_data]
    base_value_order = [category.publicDataCategory, category.labelSystemCategory, category.LLMCategory]
    base_map = dict(zip(base_key_order, base_value_order))
    base_map_without_none_values = {key: value for key, value in base_map.items() if value is not None}
    unique_values = set(base_map_without_none_values.values())

    ranked_categories = []
    rank_list = []

    if len(base_map_without_none_values) == 3:
        if len(unique_values) == 1:
            rank_list = [public_data, label_data, llm_data]
        elif len(unique_values) == 2:
            if base_map_without_none_values[public_data] == base_map_without_none_values[label_data] != \
                    base_map_without_none_values[llm_data]:
                rank_list = [public_data, label_data, llm_data]
            elif base_map_without_none_values[label_data] == base_map_without_none_values[llm_data] != \
                    base_map_without_none_values[public_data]:
                rank_list = [label_data, llm_data, public_data]
            elif base_map_without_none_values[public_data] == base_map_without_none_values[llm_data] != \
                    base_map_without_none_values[label_data]:
                rank_list = [public_data, llm_data, label_data]
        elif len(unique_values) == 3:
            rank_list = [llm_data, public_data, label_data]
    elif len(base_map_without_none_values) == 2:
        if public_data in base_map_without_none_values and label_data in base_map_without_none_values:
            if base_map_without_none_values[public_data] and base_map_without_none_values[label_data]:
                rank_list = [public_data, label_data]
        elif label_data in base_map_without_none_values and llm_data in base_map_without_none_values:
            if base_map_without_none_values[label_data] == base_map_without_none_values[llm_data]:
                rank_list = [label_data, llm_data]
            elif base_map_without_none_values[label_data] != base_map_without_none_values[llm_data]:
                rank_list = [llm_data, label_data]
        elif public_data in base_map_without_none_values and llm_data in base_map_without_none_values:
            if base_map_without_none_values[public_data] == base_map_without_none_values[llm_data]:
                rank_list = [public_data, llm_data]
            elif base_map_without_none_values[public_data] != base_map_without_none_values[llm_data]:
                rank_list = [llm_data, public_data]
    elif len(base_map_without_none_values) == 1:
        if public_data in base_map_without_none_values:
            rank_list = [public_data]
        elif label_data in base_map_without_none_values:
            rank_list = [label_data]
        elif llm_data in base_map_without_none_values:
            rank_list = [llm_data]
    if rank_list:
        for i, key in enumerate(rank_list):
            if key in base_map_without_none_values:
                ranked_categories.append({
                    "rank": i + 1,
                    "source": key,
                    "category": base_map_without_none_values[key]
                })

    return ranked_categories