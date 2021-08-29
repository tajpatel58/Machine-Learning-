function centroids = computeCentroids(X, idx, K)
%COMPUTECENTROIDS returns the new centroids by computing the means of the 
%data points assigned to each centroid.
%   centroids = COMPUTECENTROIDS(X, idx, K) returns the new centroids by 
%   computing the means of the data points assigned to each centroid. It is
%   given a dataset X where each row is a single data point, a vector
%   idx of centroid assignments (i.e. each entry in range [1..K]) for each
%   example, and K, the number of centroids. You should return a matrix
%   centroids, where each row of centroids is the mean of the data points
%   assigned to it.
%

% Useful variables
[m n] = size(X);

% You need to return the following variables correctly.
centroids = zeros(K, n);


% ====================== YOUR CODE HERE ======================
% Instructions: Go over every centroid and compute mean of all points that
%               belong to it. Concretely, the row vector centroids(i, :)
%               should contain the mean of the data points assigned to
%               centroid i.
%
% Note: You can use a for-loop over the centroids to compute this.
%

for centroid = 1:K
    % Holds the indexxes of rows where the data is closest to centroid. 
    indx_cent = find(idx == centroid);
    % Below is a spliced matrix who's rows are data closest to centroid. 
    data_cent = X(indx_cent,:);
    % Stores the value of the number of points closest to centroid. 
    num_points = length(indx_cent);
    centroids(centroid,:) = 1/num_points * sum(data_cent); 
end 
% =============================================================


end

