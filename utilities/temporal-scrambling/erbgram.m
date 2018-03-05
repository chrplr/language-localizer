function [y,xf,cf] = ERBgram(x,fs,dbthres,lowfreq,numchan,toPlot)
% [y,xf,cf] = ERBgram(x,fs,dbthres,lowfreq,numchan,toPlot)
% fs: sampling frequency
% dbthres: threshold 
% Default fs = 44100; dbthres = 60, lowfreq = 100, numchan = 64

if nargin < 6
  toPlot = 1;
end

if nargin < 5
  numchan = 64;
end

if nargin < 4
  lowfreq = 100;
end

if nargin < 3
  dbthres = 60;
end

if nargin < 2
  fs = 44100;
end

% compute coefs
[fcoefs,cf] = MakeERBFilters2(fs,numchan,lowfreq);
[B,A] = butter(2,70*2/fs);

% erb filtering
xf = ERBFilterBank2(x,fcoefs);

% clean up data
y = max(xf,0);
% smoothing
y = filter(B,A,y');
y = y';

my = max(max(y));
miny = my/(10^(dbthres/20));
y = max(y,miny);

if toPlot
  % build time axis
  t = [0:1:size(y,2)-1]/fs*1000;
  imagesc(t,[1:1:length(cf)],20*log10(y))
  f = [4:4:length(cf)];
  set(gca,'ytick',f);
  set(gca,'yticklabel',round(cf(f)));
  xlabel('Time (ms)');
  ylabel('Centre Frequency (Hz)')
end
