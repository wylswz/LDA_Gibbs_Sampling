%%group doucuments into differnet sets according to the result of k-means
%%clustering

function [docSet sigma mu] = clusterGenerate(idx,V,dimen,k)
%%idx is generated by k-means
%%V is right singular matrix from svd
%%dimen is the dimensionality when k-means is applied
%%k is number of clusters
SIZE= size(idx);
num = SIZE(1); %%number of clusters

docSet = cell(num,1);

sigma = cell(k,1);

mu =cell(k,1);  %% mu is sum divided by clusterEle
sum = cell(k,1);
squareSum = cell(k,1);
clusterCount = zeros(k,1);

for i = 1:1:k
    mu{i} = zeros(1,dimen);
    sum{i} = zeros(1,dimen);
    squareSum{i} = zeros(1,dimen);
end

for i = 1:1:num
    docSet{i} = docPoint(i,V(i,1:dimen),idx(i));
    sum{idx(i)} = sum{idx(i)} + V(i,1:dimen);
    clusterCount(idx(i)) = clusterCount(idx(i)) + 1;  %%add 1 to count of each cluster
end

for i = 1:1:k
    mu{i} = sum{i}./clusterCount(i);
end

for i = 1:1:num
    squareSum{idx(i)} = squareSum{idx(i)} + (V(i,dimen) - mu{idx(i)}).^2; 
end

for i = 1:1:k
    sigma{i} = squareSum{i}./(clusterCount(i)-1);
end

end