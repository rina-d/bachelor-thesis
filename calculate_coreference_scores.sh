#!bin/bash

# Sherlock Holmes
echo 'Sherlock Holmes: De Agra Schat, orig'
cd dutchcoref
python3 coref.py ../openboek/parses/orig/ConanDoyle_SherlockHolmesDeAgraSchat > /tmp/x.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/ConanDoyle_SherlockHolmesDeAgraSchat.conll /tmp/x.conll
cd .. 

echo ''

echo 'Sherlock Holmes: De Agra Schat, silverspelling'
cd dutchcoref
python3 coref.py ../openboek/parses/silverspelling/ConanDoyle_SherlockHolmesDeAgraSchat > /tmp/y.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/ConanDoyle_SherlockHolmesDeAgraSchat.conll /tmp/y.conll
cd .. 

echo ''

echo 'Sherlock Holmes: De Agra Schat, goldspelling'
cd dutchcoref
python3 coref.py ../openboek/parses/goldspelling/ConanDoyle_SherlockHolmesDeAgraSchat > /tmp/z.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/ConanDoyle_SherlockHolmesDeAgraSchat.conll /tmp/z.conll
cd .. 

echo ''
echo '====================================================='
echo ''

# Max Havelaar
echo 'Max Havelaar, orig'
cd dutchcoref
python3 coref.py ../openboek/parses/orig/Multatuli_MaxHavelaar > /tmp/x.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/Multatuli_MaxHavelaar.conll /tmp/x.conll
cd .. 

echo ''

echo 'Max Havelaar, silverspelling'
cd dutchcoref
python3 coref.py ../openboek/parses/silverspelling/Multatuli_MaxHavelaar > /tmp/y.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/Multatuli_MaxHavelaar.conll /tmp/y.conll
cd .. 

echo ''

echo 'Max Havelaar, goldspelling'
cd dutchcoref
python3 coref.py ../openboek/parses/goldspelling/Multatuli_MaxHavelaar > /tmp/z.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/Multatuli_MaxHavelaar.conll /tmp/z.conll
cd .. 

echo ''
echo '====================================================='
echo ''

# Titaantjes
echo 'Titaantjes, orig'
cd dutchcoref
python3 coref.py ../openboek/parses/orig/Nescio_Titaantjes > /tmp/x.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/Nescio_Titaantjes.conll /tmp/x.conll
cd .. 

echo ''

echo 'Titaantjes, silverspelling'
cd dutchcoref
python3 coref.py ../openboek/parses/silverspelling/Nescio_Titaantjes > /tmp/y.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/Nescio_Titaantjes.conll /tmp/y.conll
cd .. 

echo ''

echo 'Titaantjes, goldspelling'
cd dutchcoref
python3 coref.py ../openboek/parses/goldspelling/Nescio_Titaantjes > /tmp/z.conll
cd ../coval
python3 scorer.py ../riddlecoref/coref/Nescio_Titaantjes.conll /tmp/z.conll
cd .. 

