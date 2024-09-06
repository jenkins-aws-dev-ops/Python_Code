#!/usr/bin/perl
open(HDL,"curl https://www.wsj.com/tech/ai/microsoft-needs-a-better-seat-at-openais-table-64bc3c3b?mod=tech_lead_story | pandoc -f html -t plain |");
   while($tmp=<HDL>){
      chop $tmp;
     ##tets
      next if $tmp =~ /s+/;
      next if $tmp eq "";
      @arrTmp = split('\s+',$tmp);
      foreach $a (@arrTmp){
         if($uniqWord{$a}){
            $uniqWord{$a} += 1;
         }else{
            $uniqWord{$a} = 1;
         }
      }
  }
close HDL;
#while(($k,$v) = each %uniqWord){
#   print "$k = $v\n"
#}
print"iam test1";
foreach my $k (sort { $uniqWord{$a} <=> $uniqWord{$b}} keys %uniqWord){
   print "$k";
   for($i=0;$i<$uniqWord{$k};$i++){
      print "*";
      print "hello perl";
   }
   print "\n";
}

