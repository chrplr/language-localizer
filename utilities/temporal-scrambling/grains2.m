function [xx,xf] = grains2(x,twin,trand,xf);
% [xx,xf] = grains2(x,twin,trand,[xf]);
% -- input
% x: signal to process
% twin: length of the grains, in ms
% trand: how many ms can be jumped when swapping grains
% xf: optional, to re-use previously computed TF analysis 
% -- output
% xx: processed signal
% xf: a structure with the time/frequency analysis of x
%
% some values that produce interesting results
% grains(x,5000,10);
% grains(x,2000,10);
% grains(x,200,100);

fs = 44100;
lowfreq = 100; % lowest frequency channel
nchannels = 64; % number of frequency channels
toPlot = 0;

if nargin < 4
  % do the auditory filterbank analysis
  [y,xf] = erbgram(x,fs,60,lowfreq,nchannels,toPlot);
end

% prepare time windows
lwin = round(twin/1000*fs);
% we want to be able to divide in 2
lwin = lwin+rem(lwin,2);

win = hanning(lwin);
lxf = size(xf,2);
nwins = ceil(lxf/lwin);
npad = round(trand/1000*fs)+lwin;

% cut the time frequency in time grains
for ichan = 1:1:size(xf,1)
  xpad = [xf(ichan,:) zeros(1,npad)];
  for iwin = 1:1:2*nwins-1
    gx(ichan,iwin).data = xpad((iwin-1)*lwin/2+1:(iwin+1)*lwin/2).*win';
    gx(ichan,iwin).start = round((iwin-1)*lwin/2+1);
  end
end

% mess up the TF analysis
for ichan = 1:1:size(xf,1)
  xx(ichan,:) = zeros(size(xpad));
  for iwin = 1:1:2*nwins-1
    istart = gx(ichan,iwin).start + ceil(trand*rand(1)/1000*fs);
    xx(ichan,istart:istart+lwin-1) = xx(ichan,istart:istart+lwin-1)+gx(ichan,iwin).data;
  end
end

% reconstruct: simple sum
xx = sum(xx,1);

