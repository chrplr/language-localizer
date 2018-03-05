
for i = 1:40
    
    my_filename = sprintf('ph%03d',i);
    
    disp(sprintf('Processing %s...', my_filename));
    
    [x,SampFreq] = audioread(strcat(my_filename,'.wav'));
    
    ## [xx,xf] = grains2(x,5000,10);
    ## audiowrite(strcat(my_filename,'_rot_5000_10.wav'), xx, SampFreq);
    
    ## [xx,xf] = grains2(x,2000,10);
    ## audiowrite(strcat(my_filename,'_rot_2000_10.wav'), xx, SampFreq);
    
    ## [xx,xf] = grains2(x,200,100);
    ## audiowrite(strcat(my_filename,'_rot_200_100.wav'), xx, SampFreq);
    
    ## [xx,xf] = grains2(x,50,100);
    ## audiowrite(strcat(my_filename,'_rot_50_100.wav'), xx, SampFreq);
    
    ## [xx,xf] = grains2(x,50,200);
    ## audiowrite(strcat(my_filename,'_rot_50_200.wav'), xx, SampFreq);
    
    [xx,xf] = grains2(x, 200, 1000);
    audiowrite(strcat(my_filename, '_200_1000.wav'), xx, SampFreq);
    
end
