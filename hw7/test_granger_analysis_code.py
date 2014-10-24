from granger_analysis_code import get_gc_content

seq = "GGGGGAAAAATTTTTCCCCC" 
seq1 = "ggggaaaattttcccc" 
seq2 = "ggGGGaaAAAttTTTccCCC"
seq3 = "gggggaaaaa\ntttttccccc"


def test_gc():
	assert get_gc_content(seq) == 50   #testing upper case
	assert get_gc_content(seq1) == 50  #testing lower case
	assert get_gc_content(seq2) == 50	#testing mixed case
	assert get_gc_content(seq3) == 50	#testing multiple lines