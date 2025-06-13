
for r in \
	jgtfxcon \
	jgtapy \
	jgtcore \
	jgtutils \
	jgtpy \
	jgtml \
	jgtagentic 
	do
		echo "# $r" >> gitlog.txt
		(cd ../$r && git log --since="24 hours ago") >> gitlog.txt		
		echo "  " >> gitlog.txt
		echo "----" >> gitlog.txt
	done

coaia tash Workspace.jgwill.jgtdocs:1.gitlog -F gitlog.txt -T 2000


