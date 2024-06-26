from crawl import get_search_results, get_parse_results
from ckip_util import ckip_word_segmenter
from gsheet_util import update_results_to_gsheet
from vis import plot_keyword_frequency

if __name__ == "__main__":
    query = '心理諮商'
    search_results = get_search_results(query)
    parsed_results = get_parse_results(search_results)

    segmented_results = ckip_word_segmenter([result['content'] for result in parsed_results])

    update_results_to_gsheet(parsed_results, segmented_results)

    plot_keyword_frequency(segmented_results)